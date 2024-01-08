from PyQt6.QtWidgets import QApplication
import sys
from frontend.setupwindow import SetupWindow
from frontend.gamewindow import GameWindow
from backend.backlogic import BackLogic

class Game():
    def __init__():
        setupwindow = SetupWindow()
        gamewindow = GameWindow()
        logic = BackLogic()

if __name__ == "__main__":
    app = QApplication([])
    window = SetupWindow()
    window.show()
    sys.exit(app.exec())
