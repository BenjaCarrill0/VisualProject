from PyQt6.QtWidgets import QApplication
import sys
from frontend.setupwindow import SetupWindow

if __name__ == "__main__":
    app = QApplication([])
    window = SetupWindow()
    window.show()
    sys.exit(app.exec())
