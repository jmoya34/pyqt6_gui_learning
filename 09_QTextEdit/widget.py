import sys
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QTextEdit, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTextEdit Demo")
        self.text_edit = QTextEdit()

        # Buttons
        copy_button = QPushButton("Copy")
        copy_button.clicked.connect(self.text_edit.copy)

        cut_button = QPushButton("Cut")
        cut_button.clicked.connect(self.text_edit.cut)

        paste_button = QPushButton("Paste")
        paste_button.clicked.connect(self.text_edit.paste)

        undo_button = QPushButton("Undo")
        undo_button.clicked.connect(self.text_edit.undo)

        redo_button = QPushButton("Redo")
        redo_button.clicked.connect(self.text_edit.redo)

        # set_plain_text_button = QPushButton("Set Plain Text")
        # set_plain_text_button.clicked.connect(self.text_edit.copy)

        # set_html_button = QPushButton("Set html")
        # set_html_button.clicked.connect(self.text_edit.copy)

        clear_button = QPushButton("clear")
        clear_button.clicked.connect(self.text_edit.clear)

        Hlayout = QHBoxLayout()
        Hlayout.addWidget(copy_button)
        Hlayout.addWidget(cut_button)
        Hlayout.addWidget(paste_button)
        Hlayout.addWidget(undo_button)
        Hlayout.addWidget(redo_button)
        # Hlayout.addWidget(set_plain_text_button)
        # Hlayout.addWidget(set_html_button)
        Hlayout.addWidget(clear_button)

        v_layout = QVBoxLayout()
        v_layout.addLayout(Hlayout)
        v_layout.addWidget(self.text_edit)

        self.setLayout(v_layout)