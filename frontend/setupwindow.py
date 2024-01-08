from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton,
                             QVBoxLayout, QHBoxLayout, QGridLayout,
                             QStackedLayout)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import pyqtSignal
from frontend.parameters import (pos_x, pos_y, width, height)

class SetupWindow(QWidget):
    load_signals = pyqtSignal()
    start_new = pyqtSignal()
    load_game = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setGeometry(pos_x, pos_y, width, height)
        self.setWindowTitle("Sample Text")

        self.initial_window()
        self.load_window()
        self.full_layout = QStackedLayout()
        self.full_layout.addWidget(self.widget_init)
        self.full_layout.addWidget(self.load_widget)

        self.setLayout(self.full_layout)
    
    def initial_window(self):
        self.new_game = QPushButton("NEW GAME", self)
        self.new_game.resize(self.new_game.sizeHint())
        self.new_game.clicked.connect(self.new)

        self.load_game = QPushButton("LOAD GAME", self)
        self.load_game.resize(self.load_game.sizeHint())
        self.load_game.clicked.connect(self.load)

        self.exit_button = QPushButton("EXIT", self)
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
        
        layout_init = QGridLayout()
        layout_init.addWidget(self.background, 0, 0)
        layout_init.addLayout(bttns_lyt, 0, 0)

        self.widget_init = QWidget()
        self.widget_init.setLayout(layout_init)

    def load_window(self):

        self.back_button = QPushButton("BACK", self)
        self.back_button.resize(self.back_button.sizeHint())
        self.back_button.clicked.connect(self.back)
        back_layout = QHBoxLayout()
        back_layout.addWidget(self.back_button)
        back_layout.addStretch(1)
        back_button_layout = QVBoxLayout()
        back_button_layout.addLayout(back_layout)
        back_button_layout.addStretch(1)

        self.load_buttons_layout = QGridLayout()
        self.obtain_loads()
        
        load_layout = QGridLayout()
        load_layout.addLayout(back_button_layout, 0, 0)

        self.load_widget = QWidget()
        self.load_widget.setLayout(load_layout)

    def new(self):
        self.start_new.emit()

    def load(self):
        self.full_layout.setCurrentWidget(self.load_widget)
    
    def exit(self):
        self.close()

    def back(self):
        self.full_layout.setCurrentWidget(self.widget_init)
    
    def obtain_loads(self):
        self.load_signals.emit()

    def load_buttons(self, *args):
        pass

    def load_file(self):
        pass