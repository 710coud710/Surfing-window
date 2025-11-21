# Surfing Application Architecture

## Overview

This document describes the architecture and design patterns used in the Surfing ADL1 Data Sorting Tool.

## Design Pattern: MVP (Model-View-Presenter)

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        Main Window                          │
│  ┌──────────┐  ┌────────────────────────────────────────┐  │
│  │          │  │            Header                      │  │
│  │          │  │  [Progress: 0/0] [45%] [███████░░░]   │  │
│  │          │  └────────────────────────────────────────┘  │
│  │ Sidebar  │  ┌────────────────────────────────────────┐  │
│  │          │  │                                        │  │
│  │ Dashboard│  │          Content Area                  │  │
│  │ Process  │  │    - Dashboard / Process Files        │  │
│  │ Results  │  │    - Results Table                    │  │
│  │ Settings │  │                                        │  │
│  │ About    │  │                                        │  │
│  │          │  └────────────────────────────────────────┘  │
│  │          │  ┌────────────────────────────────────────┐  │
│  │          │  │          Terminal                      │  │
│  │          │  │  [INFO] Ready to process...           │  │
│  └──────────┘  └────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## Component Hierarchy

```
MainWindow
├── SidebarWidget
│   └── Menu Buttons (Dashboard, Process, Results, Settings, About)
├── HeaderWidget
│   ├── Title Label
│   ├── Progress Label (current/total)
│   ├── Percentage Label
│   └── Progress Bar
├── ContentStack (QStackedWidget)
│   ├── ContentWidget (Dashboard/Process)
│   │   ├── Folder Selection
│   │   ├── Filter Options (RadioButtons)
│   │   └── Process Button
│   └── ResultWidget
│       ├── Statistics Label
│       ├── Results Table
│       └── Export Button
└── TerminalWidget
    ├── Terminal Text Area
    └── Clear Button
```

## MVP Pattern Flow

```
┌──────────────────────────────────────────────────────────────┐
│                      User Interaction                        │
└─────────────────────┬────────────────────────────────────────┘
                      │
                      ▼
┌──────────────────────────────────────────────────────────────┐
│                         VIEW LAYER                           │
│  ┌────────────┐  ┌────────────┐  ┌────────────────────────┐ │
│  │  Sidebar   │  │  Header    │  │  Content/Result        │ │
│  │  Widget    │  │  Widget    │  │  Widget                │ │
│  └─────┬──────┘  └─────┬──────┘  └──────┬─────────────────┘ │
│        │                │                 │                   │
│        └────────────────┴─────────────────┘                   │
│                         │ emit signals                        │
└─────────────────────────┼─────────────────────────────────────┘
                          │
                          ▼
┌──────────────────────────────────────────────────────────────┐
│                     PRESENTER LAYER                          │
│  ┌────────────────────────────────────────────────────────┐ │
│  │              MainPresenter                             │ │
│  │  • Receives signals from View                          │ │
│  │  • Coordinates between View and Model                  │ │
│  │  • Manages threading (ProcessWorker)                   │ │
│  │  • Updates View with results                           │ │
│  └─────────────────────┬──────────────────────────────────┘ │
└────────────────────────┼─────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────┐
│                      MODEL LAYER                             │
│  ┌────────────────────────────────────────────────────────┐ │
│  │                DataModel                               │ │
│  │  • Business Logic                                      │ │
│  │  • File Processing                                     │ │
│  │  • Data Validation                                     │ │
│  │  • Statistics Calculation                              │ │
│  └────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

## Signal/Slot Connections

### View → Presenter
```python
# Main Window
view.process_requested (folder_path, filter_type)
view.export_requested ()

# Content Widget  
content.process_requested (folder_path, filter_type)

# Result Widget
result.export_requested ()
```

### Presenter → View
```python
presenter.update_progress(current, total, percentage)
presenter.reset_progress()
presenter.set_results(results)
presenter.update_statistics(stats)
presenter.log_info(message)
presenter.log_success(message)
presenter.log_error(message)
presenter.set_processing_state(is_processing)
```

## Threading Model

```
┌─────────────────────────────────────────────────────────┐
│                      Main Thread (UI)                   │
│                                                          │
│  ┌────────────┐                                         │
│  │   View     │ ──signals──▶ ┌──────────────┐          │
│  └────────────┘              │  Presenter   │          │
│                              └───────┬──────┘          │
│                                      │                  │
│                                      │ creates          │
│                                      ▼                  │
│                              ┌──────────────┐          │
│                              │ProcessWorker │          │
│                              │  (QThread)   │          │
│                              └───────┬──────┘          │
└──────────────────────────────────────┼──────────────────┘
                                       │
┌──────────────────────────────────────┼──────────────────┐
│                    Background Thread │                  │
│                                      ▼                  │
│                              ┌──────────────┐          │
│                              │    Model     │          │
│                              │ Processing   │          │
│                              └───────┬──────┘          │
│                                      │                  │
│                                      │ emit signals     │
│                                      ▼                  │
│                              progress_updated           │
│                              processing_complete        │
│                              error_occurred             │
└─────────────────────────────────────────────────────────┘
```

## Data Flow

### 1. File Processing Flow

```
User clicks "Start Processing"
    │
    ▼
ContentWidget.process_requested.emit(folder, filter)
    │
    ▼
MainWindow.process_requested.emit(folder, filter)
    │
    ▼
MainPresenter.on_process_requested(folder, filter)
    │
    ├─▶ Validate folder
    ├─▶ Create ProcessWorker thread
    ├─▶ Connect signals
    └─▶ Start worker.start()
           │
           ▼
    ProcessWorker.run() [Background Thread]
           │
           ├─▶ DataModel.process_folder()
           │       │
           │       ├─▶ Read files
           │       ├─▶ Search keywords
           │       ├─▶ Extract serial numbers
           │       └─▶ Return results
           │
           ├─▶ Emit progress_updated signals
           └─▶ Emit processing_complete(results)
                  │
                  ▼
    MainPresenter.on_processing_complete()
           │
           ├─▶ Apply filter
           ├─▶ Calculate statistics
           ├─▶ Update view
           │      │
           │      ├─▶ view.set_results()
           │      ├─▶ view.update_statistics()
           │      └─▶ view.show_results_view()
           │
           └─▶ Log messages
```

### 2. Export Flow

```
User clicks "Export"
    │
    ▼
ResultWidget.export_requested.emit()
    │
    ▼
MainWindow.export_requested.emit()
    │
    ▼
MainPresenter.on_export_requested()
    │
    ├─▶ Check if results exist
    ├─▶ Open file dialog
    ├─▶ Export to CSV
    │      │
    │      ├─▶ Write header
    │      └─▶ Write data rows
    │
    └─▶ Log success/error
```

## Class Responsibilities

### Model Layer

#### DataModel
- **Responsibility**: Business logic and data processing
- **Methods**:
  - `process_folder(folder_path)`: Process all files in folder
  - `_process_file(file_path)`: Process single file
  - `get_progress()`: Get current progress
  - `get_statistics()`: Calculate statistics
- **No UI dependencies**: Pure Python logic

### View Layer

#### MainWindow
- **Responsibility**: Main application window layout
- **Components**: Sidebar, Header, Content Stack, Terminal
- **Signals**: process_requested, export_requested

#### SidebarWidget
- **Responsibility**: Navigation menu
- **Signal**: menu_clicked(menu_name)

#### HeaderWidget
- **Responsibility**: Display progress and statistics
- **Methods**: update_progress(), reset_progress()

#### ContentWidget
- **Responsibility**: File processing controls
- **Signal**: process_requested(folder, filter)

#### ResultWidget
- **Responsibility**: Display results table
- **Signal**: export_requested()
- **Methods**: set_results(), update_statistics()

#### TerminalWidget
- **Responsibility**: Display log messages
- **Methods**: log_info(), log_success(), log_error(), log_warning()

### Presenter Layer

#### MainPresenter
- **Responsibility**: Coordinate View and Model
- **Manages**: Threading, state, data flow
- **Slots**: 
  - on_process_requested()
  - on_processing_complete()
  - on_export_requested()

#### ProcessWorker (QThread)
- **Responsibility**: Background file processing
- **Signals**:
  - progress_updated(current, total, percentage)
  - processing_complete(results)
  - error_occurred(error)

## Key Design Decisions

### 1. Why MVP?
- **Separation of Concerns**: UI, Logic, and Coordination are separate
- **Testability**: Each layer can be tested independently
- **Maintainability**: Easy to modify one layer without affecting others

### 2. Why Threading?
- **Responsive UI**: File processing doesn't block UI
- **Better UX**: Users can see progress in real-time
- **Scalability**: Can process many files without freezing

### 3. Why Modular Widgets?
- **Reusability**: Widgets can be reused in other projects
- **Maintainability**: Each widget is self-contained
- **Scalability**: Easy to add new features

### 4. Why Signals/Slots?
- **Loose Coupling**: Components don't need direct references
- **Qt Pattern**: Native to Qt framework
- **Thread-Safe**: Qt handles cross-thread communication

## File Structure

```
Surfing/
│
├─ main.py                          # Application entry point
│  └─ Creates: QApplication, Model, View, Presenter
│
├─ model/
│  └─ data_model.py                 # Business logic
│     └─ DataModel class
│
├─ views/
│  ├─ main_window.py                # Main window
│  │  └─ MainWindow(QMainWindow)
│  │
│  ├─ sidebar_widget.py             # Sidebar
│  │  └─ SidebarWidget(QWidget)
│  │
│  ├─ header_widget.py              # Header
│  │  └─ HeaderWidget(QWidget)
│  │
│  ├─ content_widget.py             # Content
│  │  └─ ContentWidget(QWidget)
│  │
│  ├─ result_widget.py              # Results
│  │  └─ ResultWidget(QWidget)
│  │
│  └─ terminal_widget.py            # Terminal
│     └─ TerminalWidget(QWidget)
│
└─ presenter/
   └─ main_presenter.py             # Coordinator
      ├─ MainPresenter(QObject)
      └─ ProcessWorker(QThread)
```

## Extension Points

### Adding New Features

1. **New Menu Item**:
   - Add to `sidebar_widget.py` menu_items list
   - Create new widget in `views/`
   - Add to content_stack in `main_window.py`

2. **New Filter Option**:
   - Add radio button in `content_widget.py`
   - Update filter logic in `main_presenter.py`

3. **New Data Processing**:
   - Add method to `data_model.py`
   - Update `ProcessWorker` if needed

4. **New Export Format**:
   - Add export method in `main_presenter.py`
   - Add button in `result_widget.py`

## Best Practices

### 1. View Layer
- ✅ Only UI code
- ✅ Emit signals for user actions
- ❌ No business logic
- ❌ No file I/O

### 2. Model Layer
- ✅ Pure Python logic
- ✅ No Qt dependencies (except QThread)
- ❌ No UI code
- ❌ No direct view updates

### 3. Presenter Layer
- ✅ Coordinates between View and Model
- ✅ Manages threading
- ✅ Updates View based on Model
- ❌ Minimal business logic

## Performance Considerations

- **Threading**: Heavy processing in background thread
- **Signals**: Efficient Qt signal/slot mechanism
- **Table**: QTableWidget with alternating row colors
- **Progress**: Real-time updates without blocking

## Security Considerations

- **File Access**: Read-only access to log files
- **Error Handling**: Try-except blocks for file I/O
- **Input Validation**: Check folder existence
- **Encoding**: UTF-8 with error handling

---

**Version**: 1.0.0  
**Last Updated**: November 2025

