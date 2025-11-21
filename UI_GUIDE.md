# Surfing - UI Design Guide

## 🎨 Visual Layout

### Full Application Layout

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Surfing - ADL1 Data Sorting Tool                                     👤    │
│                                                                              │
│  ADL1 Data Sorting Dashboard                                                │
│  220,000 / 500,000    45%    ████████████████░░░░░░░░░░░░░░░░░░             │
│──────────────────────────────────────────────────────────────────────────────│
│          │                                                                   │
│          │  Welcome to ADL1 Data Sorting Tool                               │
│          │  Select a folder containing log files and choose filter options  │
│          │                                                                   │
│          │  ┌─────────────────────────────────────────────────────────┐     │
│          │  │ 📁 Folder Selection                                    │     │
│  Surfing │  │                                                         │     │
│  ━━━━━━  │  │  [D:\Beta\Surfing\Logs                     ] [Browse]  │     │
│          │  └─────────────────────────────────────────────────────────┘     │
│ 📊 Dash  │                                                                   │
│ 🔄 Proc  │  ┌─────────────────────────────────────────────────────────┐     │
│ 📋 Res   │  │ 🔍 Filter Options                                      │     │
│ ⚙️ Set   │  │                                                         │     │
│ ℹ️ About │  │  ○ Show All Results                                    │     │
│          │  │  ○ Show Only Invalid (0xFFFFFFFF)                      │     │
│          │  │  ○ Show Only Valid                                      │     │
│          │  └─────────────────────────────────────────────────────────┘     │
│          │                                                                   │
│          │  ┌─────────────────────────────────────────────────────────┐     │
│          │  │ ℹ️ Search Keywords                                      │     │
│          │  │ • Looking for: mfg_data: 0x0A050000                    │     │
│  v1.0.0  │  │ • Invalid when: 0xFFFFFFFF                              │     │
│          │  │ • Extracts: PCBA SN No                                  │     │
│          │  └─────────────────────────────────────────────────────────┘     │
│          │                                                                   │
│          │                      [▶ Start Processing]                        │
│          │                                                                   │
│──────────┼───────────────────────────────────────────────────────────────────│
│          │ Terminal                                                  [Clear] │
│          │ ┌───────────────────────────────────────────────────────────────┐│
│          │ │ [INFO] Terminal initialized. Ready to process files...       ││
│          │ │ [INFO] Application started successfully                      ││
│          │ │                                                               ││
│          │ └───────────────────────────────────────────────────────────────┘│
└──────────┴───────────────────────────────────────────────────────────────────┘
```

---

## 📊 Results View

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Surfing - ADL1 Data Sorting Tool                                     👤    │
│                                                                              │
│  ADL1 Data Sorting Dashboard                                                │
│  15 / 20    75%    ██████████████████████████░░░░░░░░                       │
│──────────────────────────────────────────────────────────────────────────────│
│          │                                                                   │
│          │  Result            Total: 15 | Valid: 12 | Invalid: 3  [Export]  │
│          │  ┌────────────────────────────────────────────────────────────┐  │
│  Surfing │  │ #  │ File Name              │ Serial Number │ Status      │  │
│  ━━━━━━  │  ├────┼────────────────────────┼───────────────┼─────────────┤  │
│          │  │ 1  │ Hoki_ADL1_...txt      │ GT54M50354... │ ✅ Valid    │  │
│ 📊 Dash  │  │ 2  │ Hapuka_ADL1_...txt    │ GT54FJ0354... │ ❌ Invalid  │  │
│ 🔄 Proc  │  │ 3  │ Test_ADL1_...txt      │ GT54AB1234... │ ✅ Valid    │  │
│ 📋 Res   │  │ 4  │ Sample_ADL1_...txt    │ GT54CD5678... │ ✅ Valid    │  │
│ ⚙️ Set   │  │ 5  │ Data_ADL1_...txt      │ GT54EF9012... │ ❌ Invalid  │  │
│ ℹ️ About │  │ 6  │ Log_ADL1_...txt       │ GT54GH3456... │ ✅ Valid    │  │
│          │  │ 7  │ Output_ADL1_...txt    │ GT54IJ7890... │ ✅ Valid    │  │
│          │  │ 8  │ Result_ADL1_...txt    │ GT54KL1234... │ ❌ Invalid  │  │
│          │  │ 9  │ Process_ADL1_...txt   │ GT54MN5678... │ ✅ Valid    │  │
│          │  │ 10 │ Final_ADL1_...txt     │ GT54OP9012... │ ✅ Valid    │  │
│  v1.0.0  │  └────────────────────────────────────────────────────────────┘  │
│          │                                                                   │
│──────────┼───────────────────────────────────────────────────────────────────│
│          │ Terminal                                                  [Clear] │
│          │ ┌───────────────────────────────────────────────────────────────┐│
│          │ │ [INFO] Starting to process folder: D:\Beta\Surfing\Logs      ││
│          │ │ [INFO] Filter mode: all                                      ││
│          │ │ [SUCCESS] Processing complete! Found 15 items                ││
│          │ │ [INFO] Displaying 15 items after filter                      ││
│          │ │ [INFO] Navigated to: Results                                 ││
│          │ └───────────────────────────────────────────────────────────────┘│
└──────────┴───────────────────────────────────────────────────────────────────┘
```

---

## 🎨 Color Scheme

### Primary Colors
| Color | Hex Code | Usage |
|-------|----------|-------|
| Teal | `#1abc9c` | Primary buttons, active states |
| Dark Teal | `#16a085` | Hover states |
| Dark Blue | `#2c3e50` | Sidebar background |
| Darker Blue | `#34495e` | Hover on sidebar |
| Blue | `#3498db` | Action buttons |
| Light Gray | `#f8f9fa` | Content background |
| White | `#ffffff` | Cards, tables |

### Status Colors
| Status | Hex Code | Icon |
|--------|----------|------|
| Success | `#27ae60` | ✅ |
| Error | `#e74c3c` | ❌ |
| Warning | `#f39c12` | ⚠️ |
| Info | `#4a90e2` | ℹ️ |

### UI Element Colors
| Element | Background | Text | Border |
|---------|-----------|------|--------|
| Sidebar | `#2c3e50` | `#ffffff` | None |
| Header | `#ffffff` | `#2c3e50` | `#ecf0f1` |
| Content | `#f8f9fa` | `#2c3e50` | None |
| Terminal | `#1e1e1e` | `#d4d4d4` | `#3c3c3c` |
| Table Header | `#34495e` | `#ffffff` | None |

---

## 📐 Dimensions & Spacing

### Window Sizes
- **Minimum Window**: 1200px × 800px
- **Sidebar Width**: 200px (fixed)
- **Terminal Min Height**: 200px

### Spacing
- **Main Layout Margins**: 0px (full bleed)
- **Content Margins**: 15px
- **Widget Spacing**: 10-20px
- **Button Padding**: 8-15px
- **Table Cell Padding**: 8px

### Fonts
- **Title Font**: Segoe UI, 16-18pt, Bold
- **Body Font**: Segoe UI, 10-14pt, Regular
- **Terminal Font**: Consolas/Courier New, 12pt, Monospace

---

## 🎯 Component Breakdown

### 1. Sidebar (`#2c3e50`)
```
┌──────────┐
│ Surfing  │ ← Title (#1abc9c background)
├──────────┤
│ 📊 Dash  │ ← Active item
│ 🔄 Proc  │
│ 📋 Res   │
│ ⚙️ Set   │
│ ℹ️ About │
│          │
│   ...    │
│          │
│ v1.0.0   │ ← Footer
└──────────┘
```

**Features:**
- Fixed 200px width
- Dark theme (#2c3e50)
- Active highlight (#1abc9c)
- Hover effect (#34495e)
- Icons + Text labels
- Version footer

---

### 2. Header (White)
```
┌─────────────────────────────────────────────────┐
│ ADL1 Data Sorting Dashboard              👤    │
│ 220,000 / 500,000  45%  [████████░░░░░░░]      │
└─────────────────────────────────────────────────┘
```

**Features:**
- White background
- Title text (16pt bold)
- Progress counter
- Percentage label (#1abc9c)
- Progress bar with gradient
- User icon

---

### 3. Content Area (Light Gray `#f8f9fa`)

#### Dashboard Mode
```
┌─────────────────────────────────────┐
│ Welcome to ADL1 Data Sorting Tool   │
│                                     │
│ [Folder Selection Group]            │
│ [Filter Options Group]              │
│ [Keywords Info Group]               │
│                                     │
│       [▶ Start Processing]          │
└─────────────────────────────────────┘
```

**Features:**
- White card backgrounds
- Grouped sections with borders
- Centered action button
- Large, clear text

#### Results Mode
```
┌─────────────────────────────────────┐
│ Result    Stats: 15|12|3  [Export]  │
│ ┌─────────────────────────────────┐ │
│ │ Table with colored status       │ │
│ │ Alternating row colors          │ │
│ │ Sortable columns                │ │
│ └─────────────────────────────────┘ │
└─────────────────────────────────────┘
```

**Features:**
- Statistics header
- Export button
- Table with 4 columns
- Color-coded status
- Hover effects

---

### 4. Terminal (Dark `#1e1e1e`)
```
┌─────────────────────────────────────┐
│ Terminal                    [Clear] │
│ ┌─────────────────────────────────┐ │
│ │ [INFO] Message in blue          │ │
│ │ [SUCCESS] Message in green      │ │
│ │ [ERROR] Message in red          │ │
│ │ [WARNING] Message in orange     │ │
│ └─────────────────────────────────┘ │
└─────────────────────────────────────┘
```

**Features:**
- Terminal-style dark theme
- Monospace font (Consolas)
- Color-coded by type
- Clear button
- Auto-scroll
- Read-only

---

## 🖱️ Interactive Elements

### Buttons

#### Primary Button (Process)
```css
Background: #1abc9c
Hover: #16a085
Text: White
Padding: 12px 40px
Border-radius: 5px
Font-size: 15px
```

#### Secondary Button (Browse)
```css
Background: #95a5a6
Hover: #7f8c8d
Text: White
Padding: 10px 20px
Border-radius: 5px
```

#### Action Button (Export)
```css
Background: #3498db
Hover: #2980b9
Text: White
Padding: 8px 20px
Border-radius: 5px
```

#### Danger Button (Clear)
```css
Background: #e74c3c
Hover: #c0392b
Text: White
Padding: 6px 15px
Border-radius: 4px
```

---

### Input Fields

```css
Border: 2px solid #dee2e6
Focus Border: 2px solid #1abc9c
Background: White
Padding: 10px
Border-radius: 5px
Font-size: 13px
```

---

### Progress Bar

```css
Border: 2px solid #bdc3c7
Background: #ecf0f1
Height: 25px
Border-radius: 5px

Chunk (fill):
  Gradient: #1abc9c → #16a085
  Border-radius: 3px
```

---

### Table

```css
Header:
  Background: #34495e
  Text: White
  Padding: 10px
  
Rows:
  Alternating colors
  Padding: 8px
  
Selected:
  Background: #1abc9c
  Text: White
  
Status Cell:
  Valid: #27ae60 (green)
  Invalid: #e74c3c (red)
```

---

## 📱 Responsiveness

### Splitter Ratios
- **Content** : **Terminal** = 70% : 30%
- User can drag to resize
- Minimum terminal height: 200px

### Column Resizing
- **#** column: Fixed 60px
- **File Name**: Stretch (flexible)
- **Serial Number**: Stretch (flexible)
- **Status**: Fixed 120px

---

## 🎭 States & Interactions

### Processing State
- Button text changes: "▶ Start Processing" → "⏳ Processing..."
- Button disabled during processing
- Folder input disabled
- Progress bar updates in real-time
- Terminal shows live logs

### Hover States
- Sidebar items: Background → #34495e
- Buttons: Darker shade of base color
- Table rows: Subtle highlight

### Active States
- Sidebar: #1abc9c background + left border
- Radio buttons: Checked indicator
- Selected table rows: #1abc9c background

### Focus States
- Input fields: Border → #1abc9c
- Keyboard navigation supported

---

## 🌈 Icon Usage

### Emoji Icons
- 📊 Dashboard
- 🔄 Process Files
- 📋 Results
- ⚙️ Settings
- ℹ️ About
- 📁 Folder
- 🔍 Search/Filter
- 👤 User
- 📥 Export
- 🗑️ Clear
- ▶ Start/Play
- ⏳ Processing
- ✅ Valid/Success
- ❌ Invalid/Error

### Why Emojis?
- Universal understanding
- No external image dependencies
- Colorful and modern
- Cross-platform compatible

---

## 🎨 Theming System

### Current Theme: "Modern Light"

All colors are defined in component stylesheets, making it easy to create a dark theme variant:

### Potential Dark Theme Mapping
| Light | Dark |
|-------|------|
| `#ffffff` (White) | `#2c3e50` (Dark) |
| `#f8f9fa` (Light Gray) | `#1e1e1e` (Almost Black) |
| `#2c3e50` (Dark) | `#ecf0f1` (Light) |
| Keep accent colors the same |

---

## 📐 Layout Hierarchy

```
MainWindow (QMainWindow)
└── QWidget (central widget)
    └── QHBoxLayout
        ├── SidebarWidget (200px fixed)
        │   └── QVBoxLayout
        │       ├── Title Label
        │       ├── Menu Buttons × 5
        │       └── Footer Label
        │
        └── QWidget (right side)
            └── QVBoxLayout
                ├── HeaderWidget
                │   └── QVBoxLayout
                │       ├── Title + User Icon
                │       └── Progress Section
                │
                └── QSplitter (Vertical)
                    ├── QStackedWidget (70%)
                    │   ├── ContentWidget (page 0)
                    │   └── ResultWidget (page 1)
                    │
                    └── TerminalWidget (30%)
```

---

## 🎯 Design Principles Applied

1. **Clarity**: Clear labels, obvious actions
2. **Consistency**: Same patterns throughout
3. **Feedback**: Visual feedback for all actions
4. **Efficiency**: Quick access to common tasks
5. **Aesthetics**: Modern, professional appearance

---

## 💡 Best Practices Used

- ✅ Contrast ratios meet WCAG standards
- ✅ Touch-friendly button sizes (min 40×40px)
- ✅ Clear visual hierarchy
- ✅ Consistent spacing system
- ✅ Intuitive navigation
- ✅ Status indicators always visible
- ✅ Loading states for async operations
- ✅ Error states clearly communicated

---

**Version**: 1.0.0  
**Design System**: Material-inspired with custom colors  
**Framework**: PySide6 (Qt6)

