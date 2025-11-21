"""
Sidebar Widget - Navigation menu on the left side
"""
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFrame
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont


class SidebarWidget(QWidget):
    """Sidebar navigation widget"""
    
    # Signals
    menu_clicked = Signal(str)  # Emits menu item name
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the sidebar UI"""
        self.setFixedWidth(200)
        self.setStyleSheet("""
            QWidget {
                background-color: #2c3e50;
                color: white;
            }
            QPushButton {
                background-color: transparent;
                color: white;
                border: none;
                padding: 15px 20px;
                text-align: left;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #34495e;
            }
            QPushButton:pressed {
                background-color: #1abc9c;
            }
            QPushButton[active="true"] {
                background-color: #1abc9c;
                border-left: 4px solid #16a085;
            }
        """)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Logo/Title section
        title_label = QLabel("Surfing")
        title_label.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        title_label.setFont(font)
        title_label.setStyleSheet("padding: 30px 20px; background-color: #1abc9c;")
        layout.addWidget(title_label)
        
        # Separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setStyleSheet("background-color: #34495e;")
        layout.addWidget(separator)
        
        # Menu buttons
        self.menu_buttons = {}
        menu_items = [
            ("Dashboard", "📊"),
            ("Process Files", "🔄"),
            ("Results", "📋"),
            ("Settings", "⚙️"),
            ("About", "ℹ️")
        ]
        
        for name, icon in menu_items:
            btn = QPushButton(f"{icon}  {name}")
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda checked, n=name: self._on_menu_click(n))
            self.menu_buttons[name] = btn
            layout.addWidget(btn)
        
        # Set Dashboard as active by default
        self.set_active_menu("Dashboard")
        
        # Spacer
        layout.addStretch()
        
        # Footer
        footer_label = QLabel("v1.0.0")
        footer_label.setAlignment(Qt.AlignCenter)
        footer_label.setStyleSheet("padding: 20px; color: #7f8c8d; font-size: 12px;")
        layout.addWidget(footer_label)
        
    def _on_menu_click(self, menu_name: str):
        """Handle menu button click"""
        self.set_active_menu(menu_name)
        self.menu_clicked.emit(menu_name)
        
    def set_active_menu(self, menu_name: str):
        """Set the active menu item"""
        for name, btn in self.menu_buttons.items():
            if name == menu_name:
                btn.setProperty("active", "true")
            else:
                btn.setProperty("active", "false")
            btn.style().unpolish(btn)
            btn.style().polish(btn)

