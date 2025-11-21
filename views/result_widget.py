"""
Result Widget - Display processed results in a table
"""
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, 
                               QHeaderView, QHBoxLayout, QLabel, QPushButton, QFileDialog)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont, QColor


class ResultWidget(QWidget):
    """Widget to display processing results"""
    
    # Signals
    export_requested = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the result UI"""
        self.setStyleSheet("""
            QWidget {
                background-color: #f8f9fa;
            }
            QLabel {
                color: #2c3e50;
            }
            QTableWidget {
                background-color: white;
                border: 1px solid #dee2e6;
                border-radius: 5px;
                gridline-color: #dee2e6;
            }
            QTableWidget::item {
                padding: 8px;
            }
            QTableWidget::item:selected {
                background-color: #1abc9c;
                color: white;
            }
            QHeaderView::section {
                background-color: #34495e;
                color: white;
                padding: 10px;
                border: none;
                font-weight: bold;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 8px 20px;
                border-radius: 5px;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)
        
        # Header section
        header_layout = QHBoxLayout()
        
        title_label = QLabel("Result")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title_label.setFont(title_font)
        header_layout.addWidget(title_label)
        
        # Statistics labels
        self.stats_label = QLabel("Total: 0 | Valid: 0 | Invalid: 0")
        self.stats_label.setStyleSheet("color: #7f8c8d; font-size: 12px;")
        header_layout.addWidget(self.stats_label)
        
        header_layout.addStretch()
        
        # Export button
        export_btn = QPushButton("📥 Export")
        export_btn.clicked.connect(self.export_requested.emit)
        header_layout.addWidget(export_btn)
        
        layout.addLayout(header_layout)
        
        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["#", "File Name", "Serial Number", "Status"])
        
        # Configure table
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Fixed)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Fixed)
        
        self.table.setColumnWidth(0, 60)
        self.table.setColumnWidth(3, 120)
        
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        
        layout.addWidget(self.table)
        
    def set_results(self, results: list):
        """
        Set the results to display
        results: List of (filename, serial_number, is_invalid)
        """
        self.table.setRowCount(0)
        
        for idx, (filename, sn, is_invalid) in enumerate(results, 1):
            row = self.table.rowCount()
            self.table.insertRow(row)
            
            # Index
            index_item = QTableWidgetItem(str(idx))
            index_item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row, 0, index_item)
            
            # Filename
            filename_item = QTableWidgetItem(filename)
            self.table.setItem(row, 1, filename_item)
            
            # Serial Number
            sn_item = QTableWidgetItem(sn)
            self.table.setItem(row, 2, sn_item)
            
            # Status
            status = "❌ Invalid" if is_invalid else "✅ Valid"
            status_item = QTableWidgetItem(status)
            status_item.setTextAlignment(Qt.AlignCenter)
            
            if is_invalid:
                status_item.setForeground(QColor("#e74c3c"))
            else:
                status_item.setForeground(QColor("#27ae60"))
                
            self.table.setItem(row, 3, status_item)
        
    def update_statistics(self, stats: dict):
        """Update statistics display"""
        self.stats_label.setText(
            f"Total: {stats['total']} | Valid: {stats['valid']} | Invalid: {stats['invalid']}"
        )
        
    def clear_results(self):
        """Clear all results"""
        self.table.setRowCount(0)
        self.stats_label.setText("Total: 0 | Valid: 0 | Invalid: 0")

