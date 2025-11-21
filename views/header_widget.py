"""
Header Widget - Top section with progress indicators
"""
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QProgressBar, QFrame, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class HeaderWidget(QWidget):
    """Header widget with progress bar and statistics"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the header UI"""
        self.setStyleSheet("""
            QWidget {
                background-color: white;
            }
            QLabel {
                color: #2c3e50;
            }
            QProgressBar {
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                text-align: center;
                height: 25px;
                background-color: #ecf0f1;
            }
            QProgressBar::chunk {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                                  stop:0 #1abc9c, stop:1 #16a085);
                border-radius: 3px;
            }
        """)
        
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 15, 20, 15)
        
        # Top row with title and user icon
        top_row = QHBoxLayout()
        
        # Title
        title_label = QLabel("ADL1 Data Sorting Dashboard")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        top_row.addWidget(title_label)
        
        top_row.addStretch()
        
        # User icon placeholder
        user_icon = QLabel("👤")
        user_font = QFont()
        user_font.setPointSize(20)
        user_icon.setFont(user_font)
        top_row.addWidget(user_icon)
        
        main_layout.addLayout(top_row)
        
        # Progress section
        progress_layout = QHBoxLayout()
        progress_layout.setSpacing(20)
        
        # Progress stats
        stats_layout = QHBoxLayout()
        
        self.progress_label = QLabel("0 / 0")
        progress_font = QFont()
        progress_font.setPointSize(14)
        progress_font.setBold(True)
        self.progress_label.setFont(progress_font)
        stats_layout.addWidget(self.progress_label)
        
        self.percentage_label = QLabel("0%")
        percentage_font = QFont()
        percentage_font.setPointSize(16)
        percentage_font.setBold(True)
        self.percentage_label.setFont(percentage_font)
        self.percentage_label.setStyleSheet("color: #1abc9c;")
        stats_layout.addWidget(self.percentage_label)
        
        progress_layout.addLayout(stats_layout)
        
        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(True)
        progress_layout.addWidget(self.progress_bar, 1)
        
        main_layout.addLayout(progress_layout)
        
        # Separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setStyleSheet("background-color: #ecf0f1; max-height: 2px;")
        main_layout.addWidget(separator)
        
    def update_progress(self, current: int, total: int, percentage: float):
        """Update the progress indicators"""
        self.progress_label.setText(f"{current:,} / {total:,}")
        self.percentage_label.setText(f"{percentage:.1f}%")
        self.progress_bar.setValue(int(percentage))
        
    def reset_progress(self):
        """Reset progress to zero"""
        self.update_progress(0, 0, 0.0)

