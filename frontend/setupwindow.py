from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton,
                             QVBoxLayout, QHBoxLayout, QGridLayout)
from PyQt6.QtGui import QPixmap
from frontend.parameters import (pos_x, pos_y, width, height)

class SetupWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(pos_x, pos_y, width, height)
        self.setWindowTitle("Sample Text")

        self.new_game = QPushButton("NEW GAME")
        self.new_game.resize(self.new_game.sizeHint())
        self.new_game.clicked.connect(self.new)

        self.load_game = QPushButton("LOAD GAME")
        self.load_game.resize(self.load_game.sizeHint())
        self.load_game.clicked.connect(self.load)

        self.exit_button = QPushButton("EXIT")
        self.exit_button.resize(self.exit_button.sizeHint())
        self.exit_button.clicked.connect(self.exit)

        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch(1)
        buttons_layout.addWidget(self.new_game)
        buttons_layout.addWidget(self.load_game)
        buttons_layout.addWidget(self.exit_button)
        buttons_layout.addStretch(1)

        bttns_lyt = QVBoxLayout()
        bttns_lyt.addStretch(1)
        bttns_lyt.addLayout(buttons_layout)

        self.background = QLabel() #This labels
        #Would contain the background image
        
        layout = QGridLayout()
        layout.addWidget(self.background, 0, 0)
        layout.addLayout(bttns_lyt, 0, 0)

        self.setLayout(layout)


    def new(self):
        pass

    def load(self):
        pass
    
    def exit(self):
        pass