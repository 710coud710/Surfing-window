"""
Content Widget - Main content area with file processing controls
"""
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                               QPushButton, QLineEdit, QFileDialog, QGroupBox,
                               QRadioButton, QButtonGroup, QFrame)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont


class ContentWidget(QWidget):
    """Main content widget for file processing"""
    
    # Signals
    process_requested = Signal(str, str)  # folder_path, filter_type
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the content UI"""
        self.setStyleSheet("""
            QWidget {
                background-color: #f8f9fa;
            }
            QLabel {
                color: #2c3e50;
            }
            QGroupBox {
                background-color: white;
                border: 2px solid #dee2e6;
                border-radius: 8px;
                margin-top: 10px;
                font-weight: bold;
                padding: 15px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 15px;
                padding: 0 5px;
                color: #2c3e50;
            }
            QLineEdit {
                padding: 10px;
                border: 2px solid #dee2e6;
                border-radius: 5px;
                background-color: white;
                font-size: 13px;
            }
            QLineEdit:focus {
                border: 2px solid #1abc9c;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px 25px;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton#browseBtn {
                background-color: #95a5a6;
                padding: 10px 20px;
            }
            QPushButton#browseBtn:hover {
                background-color: #7f8c8d;
            }
            QPushButton#processBtn {
                background-color: #1abc9c;
                padding: 12px 40px;
                font-size: 15px;
            }
            QPushButton#processBtn:hover {
                background-color: #16a085;
            }
            QRadioButton {
                color: #2c3e50;
                spacing: 8px;
                font-size: 13px;
            }
            QRadioButton::indicator {
                width: 18px;
                height: 18px;
            }
        """)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(20)
        
        # Welcome section
        welcome_label = QLabel("Welcome to ADL1 Data Sorting Tool")
        welcome_font = QFont()
        welcome_font.setPointSize(18)
        welcome_font.setBold(True)
        welcome_label.setFont(welcome_font)
        welcome_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(welcome_label)
        
        desc_label = QLabel("Select a folder containing log files and choose your filter options")
        desc_label.setAlignment(Qt.AlignCenter)
        desc_label.setStyleSheet("color: #7f8c8d; font-size: 13px; margin-bottom: 20px;")
        layout.addWidget(desc_label)
        
        # Folder selection group
        folder_group = QGroupBox("📁 Folder Selection")
        folder_layout = QVBoxLayout()
        
        folder_input_layout = QHBoxLayout()
        
        self.folder_input = QLineEdit()
        self.folder_input.setPlaceholderText("Select a folder containing log files...")
        folder_input_layout.addWidget(self.folder_input, 1)
        
        browse_btn = QPushButton("Browse")
        browse_btn.setObjectName("browseBtn")
        browse_btn.clicked.connect(self._browse_folder)
        folder_input_layout.addWidget(browse_btn)
        
        folder_layout.addLayout(folder_input_layout)
        folder_group.setLayout(folder_layout)
        layout.addWidget(folder_group)
        
        # Filter options group
        filter_group = QGroupBox("🔍 Filter Options")
        filter_layout = QVBoxLayout()
        
        self.filter_button_group = QButtonGroup(self)
        
        self.radio_all = QRadioButton("Show All Results")
        self.radio_all.setChecked(True)
        self.filter_button_group.addButton(self.radio_all)
        filter_layout.addWidget(self.radio_all)
        
        self.radio_invalid = QRadioButton("Show Only Invalid (0xFFFFFFFF)")
        self.filter_button_group.addButton(self.radio_invalid)
        filter_layout.addWidget(self.radio_invalid)
        
        self.radio_valid = QRadioButton("Show Only Valid")
        self.filter_button_group.addButton(self.radio_valid)
        filter_layout.addWidget(self.radio_valid)
        
        filter_group.setLayout(filter_layout)
        layout.addWidget(filter_group)
        
        # Keywords info group
        info_group = QGroupBox("ℹ️ Search Keywords")
        info_layout = QVBoxLayout()
        
        info_text = QLabel(
            "• Looking for: mfg_data: 0x0A050000\n"
            "• Invalid when: 0xFFFFFFFF\n"
            "• Extracts: PCBA SN No"
        )
        info_text.setStyleSheet("color: #7f8c8d; font-size: 12px; padding: 5px;")
        info_layout.addWidget(info_text)
        
        info_group.setLayout(info_layout)
        layout.addWidget(info_group)
        
        layout.addStretch()
        
        # Process button
        process_btn_layout = QHBoxLayout()
        process_btn_layout.addStretch()
        
        self.process_btn = QPushButton("▶ Start Processing")
        self.process_btn.setObjectName("processBtn")
        self.process_btn.clicked.connect(self._on_process_clicked)
        self.process_btn.setCursor(Qt.PointingHandCursor)
        process_btn_layout.addWidget(self.process_btn)
        
        process_btn_layout.addStretch()
        layout.addLayout(process_btn_layout)
        
    def _browse_folder(self):
        """Open folder browser dialog"""
        folder = QFileDialog.getExistingDirectory(
            self,
            "Select Folder",
            "",
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        )
        if folder:
            self.folder_input.setText(folder)
            
    def _on_process_clicked(self):
        """Handle process button click"""
        folder_path = self.folder_input.text().strip()
        if not folder_path:
            return
            
        # Determine filter type
        if self.radio_invalid.isChecked():
            filter_type = "invalid"
        elif self.radio_valid.isChecked():
            filter_type = "valid"
        else:
            filter_type = "all"
            
        self.process_requested.emit(folder_path, filter_type)
        
    def set_processing_state(self, is_processing: bool):
        """Enable/disable controls during processing"""
        self.process_btn.setEnabled(not is_processing)
        self.folder_input.setEnabled(not is_processing)
        
        if is_processing:
            self.process_btn.setText("⏳ Processing...")
        else:
            self.process_btn.setText("▶ Start Processing")

