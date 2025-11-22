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
                color: white;
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
        
        # Logo/Title section with modern design
        logo_container = QWidget()
        # logo_container.setStyleSheet("""
        #     QWidget {
        #         background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        #                                    stop:0 #1abc9c, stop:1 #16a085);
        #         padding: 20px;
        #     }
        # """)
        logo_layout = QHBoxLayout(logo_container)
        logo_layout.setContentsMargins(15, 20, 15, 20)
        logo_layout.setSpacing(10)
        
        # Logo icon
        logo_icon = QLabel("logo.ico")
        logo_icon_font = QFont()
        logo_icon_font.setPointSize(28)
        logo_icon.setFont(logo_icon_font)
        logo_layout.addWidget(logo_icon)
        
        # Title text
        title_label = QLabel("Surfing")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)    
        title_font.setFamily("Segoe UI")
        title_label.setFont(title_font)
        title_label.setStyleSheet("color: white; background: transparent;")
        logo_layout.addWidget(title_label)
        
        logo_layout.addStretch()
        layout.addWidget(logo_container)
        
        # Separator with gradient
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFixedHeight(2)
        separator.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                       stop:0 transparent, 
                                       stop:0.5 rgba(255, 255, 255, 0.3), 
                                       stop:1 transparent);
        """)
        layout.addWidget(separator)
        
        # Add spacing before menu
        layout.addSpacing(15)
        
        # Menu section label
        menu_label = QLabel("MENU")
        menu_label.setStyleSheet("""
            color: rgba(255, 255, 255, 0.5);
            font-size: 11px;
            font-weight: bold;
            padding: 5px 20px;
            letter-spacing: 1px;
            background: transparent;
        """)
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
            color: rgba(255, 255, 255, 0.6);
            font-size: 11px;
            background: transparent;
        """)
        footer_layout.addWidget(version_label)
        
        copyright_label = QLabel("© 2025 Surfing")
        copyright_label.setAlignment(Qt.AlignCenter)
        copyright_label.setStyleSheet("""
            color: rgba(255, 255, 255, 0.4);
            font-size: 10px;
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
            else:
                btn.setProperty("active", "false")
            btn.style().unpolish(btn)
            btn.style().polish(btn)

