"""
Terminal Widget - Display log messages and output
"""
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLabel, QHBoxLayout, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QTextCursor, QColor
import sys
from PySide6.QtWidgets import QApplication

class TerminalWidget(QWidget):
    """Terminal-like widget for displaying logs"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the terminal UI"""
        self.setStyleSheet("""
            QWidget {
                background-color: #f8f9fa;
            }
            QLabel {
                color: #2c3e50;
            }
            QTextEdit {
                background-color: #1e1e1e;
                color: #d4d4d4;
                border: 1px solid #3c3c3c;
                border-radius: 5px;
                font-family: 'Consolas', 'Courier New', monospace;
                font-size: 12px;
                padding: 10px;
            }
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 6px 15px;
                border-radius: 4px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)
        
        # Header
        header_layout = QHBoxLayout()
        
        title_label = QLabel("Terminal")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title_label.setFont(title_font)
        header_layout.addWidget(title_label)
        
        header_layout.addStretch()
        
        # Clear button
        clear_btn = QPushButton("Clear")
        clear_btn.clicked.connect(self.clear_terminal)
        header_layout.addWidget(clear_btn)
        
        layout.addLayout(header_layout)
        
        # Terminal text area
        self.terminal_text = QTextEdit()
        self.terminal_text.setReadOnly(True)
        self.terminal_text.setMinimumHeight(200)
        layout.addWidget(self.terminal_text)
        
        # Initial message
        self.log_info("Terminal initialized. Ready to process files...")
        
    def log_info(self, message: str):
        """Log an info message"""
        self._append_message(f"[INFO] {message}", "#4a90e2")

    def log_success(self, message: str):
        """Log a success message"""
        self._append_message(f"[SUCCESS] {message}", "#27ae60")
        
    def log_error(self, message: str):
        """Log an error message"""
        self._append_message(f"[ERROR] {message}", "#e74c3c")
        
    def log_warning(self, message: str):
        """Log a warning message"""
        self._append_message(f"[WARNING] {message}", "#f39c12")
        
    def _append_message(self, message: str, color: str):
        """Append a colored message to the terminal"""
        self.terminal_text.setTextColor(QColor(color))
        self.terminal_text.append(message)
        self.terminal_text.moveCursor(QTextCursor.End)
        
    def clear_terminal(self):
        """Clear the terminal"""
        self.terminal_text.clear()
        self.log_info("Terminal cleared.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TerminalWidget()
    window.show()
    sys.exit(app.exec())



