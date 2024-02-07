import sys
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel and QLineEdit")

        # Set of signals
        label = QLabel("Full Name: ")
        self.line_edit = QLineEdit()

        button = QPushButton("Confirm")
        button.clicked.connect(self.on_button_clicked)
        self.text_holder_label = QLabel("I am here")

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label)

        self.setLayout(v_layout)

    # Creating a slot to recieve info 
    def on_button_clicked(self):
        text = self.line_edit.text()
        print("Full name:", text)
        self.text_holder_label.setText(text)
