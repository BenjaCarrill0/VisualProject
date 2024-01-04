#This file contains the class of the GameWindow
from PyQt6.QtWidgets import (QWidget, QLabel, QHBoxLayout, QVBoxLayout,
                             QPushButton, QGridLayout)
from PyQt6.QtGui import QPixmap
from frontend.parameters import (pos_x, pos_y, width, height)

class GameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_gui()
    def init_gui(self):
        self.setGeometry(pos_x, pos_y, width, height)
        self.setWindowTitle("Sample Text") #Change the name using the novel

        self.char_name = QLabel("Name", self)
        layout_char_name = QHBoxLayout()
        layout_char_name.addWidget(self.char_name)
        layout_char_name.addStretch(1)

        self.text = QLabel("Text", self)

        self.save_button = QPushButton("SAVE", self)
        self.save_button.resize(self.save_button.sizeHint())
        self.save_button.clicked.connect(self.save)
        self.exit_button = QPushButton("EXIT", self)
        self.exit_button.resize(self.exit_button.sizeHint())
        self.exit_button.clicked.connect(self.exit)
        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.save_button)
        layout_buttons.addStretch(1)
        layout_buttons.addWidget(self.exit_button)

        layout_txt = QVBoxLayout()
        layout_txt.addStretch(1)
        layout_txt.addLayout(layout_char_name)
        layout_txt.addWidget(self.text)
        layout_txt.addLayout(layout_buttons)
        txt = QWidget()
        txt.setLayout(layout_txt)

        self.background = QLabel() #This label is for the background

        characters_layout = QHBoxLayout()
        char = QWidget()
        char.setLayout(characters_layout)

        layouts = QGridLayout()
        layouts.addWidget(self.background, 0, 0)
        layouts.addWidget(char, 0, 0)
        layouts.addWidget(txt, 0, 0)

        self.setLayout(layouts)

    def save(self):
        pass
    def exit(self):
        pass