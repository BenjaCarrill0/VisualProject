from PyQt6.QtWidgets import QApplication
import sys
from frontend.gamewindow import GameWindow

if __name__ == "__main__":
    app = QApplication([])
    window = GameWindow()
    window.show()
    sys.exit(app.exec())
