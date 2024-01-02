#This file contains the class of the GameWindow
from PyQt6.QtWidgets import (QWidget, QLabel, QHBoxLayout, QVBoxLayout,
                             QPushButton)

class GameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_gui()
    def init_gui(self):
        self.setGeometry(0, 0, 700, 400)
        self.setWindowTitle("Sample Text") #Change the name using the novel

        self.char_name = QLabel("Name", self)
        layout_char_name = QHBoxLayout()
        layout_char_name.addWidget(self.char_name)
        layout_char_name.addStretch(1)

        self.text = QLabel("Text", self)

        self.save = QPushButton("SAVE", self)
        self.save.resize(self.save.sizeHint())
        self.save.clicked.connect(self.save)
        self.exit = QPushButton("EXIT", self)
        self.exit.resize(self.exit.sizeHint())
        self.exit.clicked.connect(self.exit)
        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.save)
        layout_buttons.addStretch(1)
        layout_buttons.addWidget(self.exit)

        layout_txt = QVBoxLayout()
        layout_txt.addLayout(layout_char_name)
        layout_txt.addWidget(self.text)
        layout_txt.addLayout(layout_buttons)
    
    def save(self):
        pass
    def exit(self):
        pass