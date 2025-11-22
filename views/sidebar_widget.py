"""
Sidebar Widget - Navigation menu on the left side
"""
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFrame, QHBoxLayout
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont, QPixmap
from pathlib import Path


class SidebarWidget(QWidget):
    """Sidebar navigation widget"""
    
    # Signals
    menu_clicked = Signal(str)  # Emits menu item name
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the sidebar UI"""
        self.setFixedWidth(220)
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                           stop:0 #1e3c72, stop:1 #2a5298);
                color: #2e2b2b;
            }
            QPushButton {
                background-color: transparent;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 12px 15px;
                text-align: left;
                font-size: 13px;
                margin: 4px 10px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.15);
                border-left: 3px solid #1abc9c;
            }
            QPushButton:pressed {
                background-color: rgba(26, 188, 156, 0.3);
            }
            QPushButton[active="true"] {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                           stop:0 #1abc9c, stop:1 #16a085);
                border-left: 4px solid #0e7c68;
                font-weight: bold;
            }
        """)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        """_________________LOGO_________________"""
        # Logo/Title section with modern design
        logo_container = QWidget()
        logo_container.setStyleSheet("""
            QWidget {
                background: gradient(x1:0, y1:0, x2:1, y2:1,
                                   stop:0 #1e3c72, stop:1 #2a5298);
            }
        """)
        logo_layout = QHBoxLayout(logo_container)
        
        logo_layout.setContentsMargins(15, 10, 15, 10)
        logo_layout.setSpacing(10)
        # Logo icon
        logo_icon = QLabel()
        logo_pixmap = QPixmap("assets/images/surfing3.png")
        logo_icon.setPixmap(logo_pixmap.scaled(82, 82, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        logo_icon.setStyleSheet("background: transparent;")
        logo_icon.setFixedSize(82, 82)
        logo_layout.addWidget(logo_icon)
        
        # Title text
        title_label = QLabel("Surfing")
        title_font = QFont()
        title_font.setPointSize(20)
        title_font.setBold(True)    
        title_font.setFamily("Segoe UI")
        title_label.setFont(title_font)
        title_label.setStyleSheet("color: #ffffff; background: transparent;")
        logo_layout.addWidget(title_label)
        
        logo_layout.addStretch()
        layout.addWidget(logo_container)
        
        """______________MENu________________"""
        # Separator with gradient
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFixedHeight(1)
        separator.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                       stop:0 transparent, 
                                       stop:0.5 rgba(255, 255, 255, 0.3), 
                                       stop:1 transparent);
        """)
        layout.addWidget(separator)
        
        # Add spacing before menu
        layout.addSpacing(5)
        
        # Menu section label
        menu_label = QLabel("MENU")
        menu_label.setStyleSheet("color: #000000; font-size: 18px; font-weight: bold; padding: 5px 20px; letter-spacing: 1px; background: transparent;")
        layout.addWidget(menu_label)
        
        layout.addSpacing(5)
        
        # Menu buttons with icons
        self.menu_buttons = {}
        menu_items = [
            ("Dashboard", "📊", "Main dashboard view"),
            ("Process Files", "🔄", "Process log files"),
            ("Results", "📋", "View results"),
            ("Settings", "⚙️", "Application settings"),
            ("About", "ℹ️", "About this app")
        ]
        
        for name, icon, tooltip in menu_items:
            btn = QPushButton(f"{icon}  {name}")
            btn.setCursor(Qt.PointingHandCursor)
            btn.setToolTip(tooltip)
            btn.clicked.connect(lambda checked, n=name: self._on_menu_click(n))
            self.menu_buttons[name] = btn
            layout.addWidget(btn)
        
        # Set Dashboard as active by default
        self.set_active_menu("Dashboard")
        
        # Spacer
        layout.addStretch()
        
        # Separator before footer
        footer_separator = QFrame()
        footer_separator.setFrameShape(QFrame.HLine)
        footer_separator.setFixedHeight(1)
        footer_separator.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);")
        layout.addWidget(footer_separator)
        
        # Footer with version and info
        footer_container = QWidget()
        footer_container.setStyleSheet("background: transparent;")
        footer_layout = QVBoxLayout(footer_container)
        footer_layout.setContentsMargins(15, 15, 15, 15)
        footer_layout.setSpacing(5)
        
        version_label = QLabel("Version 1.0.0")
        version_label.setAlignment(Qt.AlignCenter)
        version_label.setStyleSheet("""
            color: #000000;
            font-size: 15px;
            background: transparent;
        """)
        footer_layout.addWidget(version_label)
        
        copyright_label = QLabel("© 2025 Surfing")
        copyright_label.setAlignment(Qt.AlignCenter)
        copyright_label.setStyleSheet("""
            color: #000000;
            font-size: 15px;
            background: transparent;
        """)
        footer_layout.addWidget(copyright_label)
        
        layout.addWidget(footer_container)
        
    def _on_menu_click(self, menu_name: str):
        """Handle menu button click"""
        self.set_active_menu(menu_name)
        self.menu_clicked.emit(menu_name)
        
    def set_active_menu(self, menu_name: str):
        """Set the active menu item"""
        for name, btn in self.menu_buttons.items():
            if name == menu_name:
                btn.setProperty("active", "true")
                btn.setStyleSheet("color: #ffffff; font-weight: bold;")
            else:
                btn.setProperty("active", "false")
                btn.setStyleSheet("color: #2e2b2b; font-weight: normal;")
            btn.style().unpolish(btn)
            btn.style().polish(btn)

