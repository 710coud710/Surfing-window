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
        
        # Currently only one option available
        self.radio_invalid = QRadioButton("Show Invalid Files (mfg_data: 0xFFFFFFFF)")
        self.radio_invalid.setChecked(True)
        self.filter_button_group.addButton(self.radio_invalid)

             # Currently only one option available
        self.seclect_sample = QRadioButton("Option feature coming soon")
        # self.seclect_sample.setChecked(True)
        self.filter_button_group.addButton(self.seclect_sample)
        self.seclect_sample2 = QRadioButton("Option feature coming soon 2")
        # self.seclect_sample.setChecked(True)
        self.filter_button_group.addButton(self.seclect_sample2)

        filter_layout.addWidget(self.radio_invalid)
        filter_layout.addWidget(self.seclect_sample)
        filter_layout.addWidget(self.seclect_sample2)
        # ─────────────────────────────────────────────────────────────
        # TODO: Add more filter options here in future updates
        # ─────────────────────────────────────────────────────────────
        
        filter_group.setLayout(filter_layout)
        layout.addWidget(filter_group)
        
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
        """Open folder browser dialog - using Windows native dialog"""
        # Get current folder path if exists
        current_path = self.folder_input.text().strip()
        start_path = current_path if current_path else ""
        
        # Use native Windows dialog (prettier and familiar)
        folder = QFileDialog.getExistingDirectory(
            self,
            "Select Folder Containing Log Files",
            start_path,
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        )
        
        if folder:
            self.folder_input.setText(folder)


            
    def _on_process_clicked(self):
        """Handle process button click"""
        folder_path = self.folder_input.text().strip()
        if not folder_path:
            return
            
        # Currently only one filter option: Invalid
        filter_type = "invalid"
            
        self.process_requested.emit(folder_path, filter_type)
        
    def set_processing_state(self, is_processing: bool):
        """Enable/disable controls during processing"""
        self.process_btn.setEnabled(not is_processing)
        self.folder_input.setEnabled(not is_processing)
        
        if is_processing:
            self.process_btn.setText("⏳ Processing...")
        else:
            self.process_btn.setText("▶ Start Processing")

