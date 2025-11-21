Surfing/
├─ main.py                      # Khởi tạo app
├─ views/
│   ├─ __init__.py
│   ├─ main_window.py           # Main window layout
│   ├─ sidebar_widget.py        # Sidebar navigation
│   ├─ header_widget.py         # Header with progress
│   ├─ content_widget.py        # File processing controls
│   ├─ result_widget.py         # Results table
│   └─ terminal_widget.py       # Terminal logs
├─ model/                       # Xử lý dữ liệu, logic nghiệp vụ
│   ├─ __init__.py
│   └─ data_model.py            # Data processing logic
├─ presenter/                   # Điều phối View <-> Model, quản lý thread
│   ├─ __init__.py
│   └─ main_presenter.py        # MVP coordinator + threading
└─ requirements.txt             # PySide6>=6.6.0