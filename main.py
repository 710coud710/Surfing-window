"""
Main entry point for the Surfing application
"""
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFont

from views.main_window import MainWindow
from model.data_model import DataModel
from presenter.main_presenter import MainPresenter


def main():
    """Main application entry point"""
    app = QApplication(sys.argv)
    
    # Set application properties
    app.setApplicationName("Surfing")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("ADL1 Tools")
    
    # Set default font
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    
    # Create MVC components
    model = DataModel()
    view = MainWindow()
    presenter = MainPresenter(view, model)
    
    # Show window
    view.show()
    
    # Run application
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

