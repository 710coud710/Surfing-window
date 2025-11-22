from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFontDatabase
import sys  

app = QApplication(sys.argv)

for family in QFontDatabase().families():
    print(family)

sys.exit(app.exec())
