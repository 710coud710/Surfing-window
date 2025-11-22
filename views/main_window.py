"""
Main Window - The main application window with layout
"""
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                               QStackedWidget, QSplitter)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIcon

from .sidebar_widget import SidebarWidget
from .header_widget import HeaderWidget
from .content_widget import ContentWidget
from .result_widget import ResultWidget
from .terminal_widget import TerminalWidget


class MainWindow(QMainWindow):
    """Main application window"""
    
    # Signals
    process_requested = Signal(str, str)  # folder_path, filter_type
    export_requested = Signal()
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the main window UI"""
        self.setWindowTitle("Surfing - Pro Program Data Sorting")
        self.setMinimumSize(1200, 800)
        
        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Sidebar
        self.sidebar = SidebarWidget()
        self.sidebar.menu_clicked.connect(self._on_menu_changed)
        main_layout.addWidget(self.sidebar)
        
        # Right side content
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)
        
        # Header
        self.header = HeaderWidget()
        self.header.toggle_sidebar.connect(self._toggle_sidebar)
        right_layout.addWidget(self.header)
        
        # Content area with splitter
        self.splitter = QSplitter(Qt.Vertical)
        
        # Stacked widget for different content views
        self.content_stack = QStackedWidget()
        
        # Dashboard/Processing view
        self.content_widget = ContentWidget()
        self.content_widget.process_requested.connect(self.process_requested.emit)
        self.content_stack.addWidget(self.content_widget)
        
        # Result view
        self.result_widget = ResultWidget()
        self.result_widget.export_requested.connect(self.export_requested.emit)
        self.content_stack.addWidget(self.result_widget)
        
        self.splitter.addWidget(self.content_stack)
        
        # Terminal
        self.terminal = TerminalWidget()
        self.splitter.addWidget(self.terminal)
        
        # Set initial splitter sizes (70% content, 30% terminal)
        self.splitter.setStretchFactor(0, 7)
        self.splitter.setStretchFactor(1, 3)
        
        right_layout.addWidget(self.splitter)
        
        main_layout.addWidget(right_widget, 1)
        
        # Apply stylesheet
        self.setStyleSheet("""
            QMainWindow {
                background-color: #ecf0f1;
            }
            QSplitter::handle {
                background-color: #bdc3c7;
                height: 2px;
            }
            QSplitter::handle:hover {
                background-color: #95a5a6;
            }
        """)
        
    def _on_menu_changed(self, menu_name: str):
        """Handle menu change"""
        self.terminal.log_info(f"Navigated to: {menu_name}")
        
        if menu_name == "Dashboard" or menu_name == "Process Files":
            self.content_stack.setCurrentWidget(self.content_widget)
        elif menu_name == "Results":
            self.content_stack.setCurrentWidget(self.result_widget)
        elif menu_name == "Settings":
            self.terminal.log_info("Settings page - Coming soon!")
        elif menu_name == "About":
            self.terminal.log_info("Surfing v1.0.0 - ADL1 Data Sorting Tool")
            self.terminal.log_info("Developed for sorting ADL1 test log data")
            
    # Public methods for presenter to interact with
    
    def update_progress(self, current: int, total: int, percentage: float):
        """Update progress indicators"""
        self.header.update_progress(current, total, percentage)
        
    def reset_progress(self):
        """Reset progress"""
        self.header.reset_progress()
        
    def set_results(self, results: list):
        """Set results in result widget"""
        self.result_widget.set_results(results)
        
    def update_statistics(self, stats: dict):
        """Update statistics"""
        self.result_widget.update_statistics(stats)
        
    def log_info(self, message: str):
        """Log info message"""
        self.terminal.log_info(message)
        
    def log_success(self, message: str):
        """Log success message"""
        self.terminal.log_success(message)
        
    def log_error(self, message: str):
        """Log error message"""
        self.terminal.log_error(message)
        
    def log_warning(self, message: str):
        """Log warning message"""
        self.terminal.log_warning(message)
        
    def set_processing_state(self, is_processing: bool):
        """Set processing state"""
        self.content_widget.set_processing_state(is_processing)
        
    def show_results_view(self):
        """Switch to results view"""
        self.content_stack.setCurrentWidget(self.result_widget)
        self.sidebar.set_active_menu("Results")
    
    def _toggle_sidebar(self):
        """Toggle sidebar visibility"""
        if self.sidebar.isVisible():
            self.sidebar.hide()
            self.terminal.log_info("Sidebar hidden - More workspace available")
        else:
            self.sidebar.show()
            self.terminal.log_info("Sidebar shown")

