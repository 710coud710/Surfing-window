"""
Main Presenter - Coordinates between View and Model, manages threading
"""
from PySide6.QtCore import QObject, QThread, Signal, Slot
from PySide6.QtWidgets import QFileDialog, QMessageBox
import csv
from pathlib import Path


class ProcessWorker(QThread):
    """Worker thread for processing files"""
    
    # Signals
    progress_updated = Signal(int, int, float)
    processing_complete = Signal(list)
    error_occurred = Signal(str)
    
    def __init__(self, model, folder_path: str):
        super().__init__()
        self.model = model
        self.folder_path = folder_path
        
    def run(self):
        """Run the processing in background thread"""
        try:
            results = self.model.process_folder(self.folder_path)
            
            # Emit final progress
            current, total, percentage = self.model.get_progress()
            self.progress_updated.emit(current, total, percentage)
            
            # Emit completion
            self.processing_complete.emit(results)
            
        except Exception as e:
            self.error_occurred.emit(str(e))


class MainPresenter(QObject):
    """Main presenter coordinating view and model"""
    
    def __init__(self, view, model):
        super().__init__()
        self.view = view
        self.model = model
        self.worker = None
        self.current_results = []
        self.filter_type = "all"
        
        # Connect view signals
        self.view.process_requested.connect(self.on_process_requested)
        self.view.export_requested.connect(self.on_export_requested)
        
        self.view.log_info("Application started successfully")
        
    @Slot(str, str)
    def on_process_requested(self, folder_path: str, filter_type: str):
        """Handle process request from view"""
        if not folder_path:
            self.view.log_error("Please select a folder first")
            return
            
        folder = Path(folder_path)
        if not folder.exists():
            self.view.log_error(f"Folder does not exist: {folder_path}")
            return
            
        self.filter_type = filter_type
        self.view.log_info(f"Starting to process folder: {folder_path}")
        self.view.log_info(f"Filter mode: {filter_type}")
        self.view.set_processing_state(True)
        self.view.reset_progress()
        
        # Create and start worker thread
        self.worker = ProcessWorker(self.model, folder_path)
        self.worker.progress_updated.connect(self.on_progress_updated)
        self.worker.processing_complete.connect(self.on_processing_complete)
        self.worker.error_occurred.connect(self.on_error_occurred)
        self.worker.finished.connect(self.on_worker_finished)
        self.worker.start()
        
    @Slot(int, int, float)
    def on_progress_updated(self, current: int, total: int, percentage: float):
        """Handle progress update"""
        self.view.update_progress(current, total, percentage)
        
    @Slot(list)
    def on_processing_complete(self, results: list):
        """Handle processing completion"""
        self.current_results = results
        
        # Apply filter
        filtered_results = self._apply_filter(results, self.filter_type)
        
        self.view.log_success(f"Processing complete! Found {len(results)} items")
        self.view.log_info(f"Displaying {len(filtered_results)} items after filter")
        
        # Update view
        self.view.set_results(filtered_results)
        
        # Get and display statistics (based on all results, not filtered)
        stats = self.model.get_statistics()
        self.view.update_statistics(stats)
        
        # Switch to results view
        self.view.show_results_view()
        
    @Slot(str)
    def on_error_occurred(self, error_message: str):
        """Handle error"""
        self.view.log_error(f"Error during processing: {error_message}")
        
    @Slot()
    def on_worker_finished(self):
        """Handle worker thread finished"""
        self.view.set_processing_state(False)
        self.worker = None
        
    def _apply_filter(self, results: list, filter_type: str) -> list:
        """Apply filter to results"""
        if filter_type == "invalid":
            return [r for r in results if r[2]]  # r[2] is is_invalid
        elif filter_type == "valid":
            return [r for r in results if not r[2]]
        else:
            return results
            
    @Slot()
    def on_export_requested(self):
        """Handle export request"""
        if not self.current_results:
            self.view.log_warning("No results to export")
            return
            
        # Open save file dialog
        file_path, _ = QFileDialog.getSaveFileName(
            self.view,
            "Export Results",
            "results.csv",
            "CSV Files (*.csv);;All Files (*)"
        )
        
        if not file_path:
            return
            
        try:
            self._export_to_csv(file_path, self.current_results)
            self.view.log_success(f"Results exported to: {file_path}")
        except Exception as e:
            self.view.log_error(f"Export failed: {str(e)}")
            
    def _export_to_csv(self, file_path: str, results: list):
        """Export results to CSV file"""
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write header
            writer.writerow(['#', 'File Name', 'Serial Number', 'Status', 'Check Time'])
            
            # Write data
            for idx, (filename, sn, is_invalid, check_time) in enumerate(results, 1):
                status = 'Invalid' if is_invalid else 'Valid'
                writer.writerow([idx, filename, sn, status, check_time])

