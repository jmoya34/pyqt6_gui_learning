from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout

# By the way QHBoxLayout makes horizontal while QVBoxLayout will make it vertical

class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RockWidget")
        button1 = QPushButton("Button1") #creates a button but doesn't lay it out anywhere
        button1.clicked.connect(self.button1_clicked)
        button2 = QPushButton("Button2")
        button2.clicked.connect(self.button2_clicked)
        # One method to lay out button horizontally or vertical is to use Layout
        button_layout = QVBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        self.setLayout(button_layout)
        
    def button1_clicked(self):
        print("Button one clicked")

    def button2_clicked(self):
        print("Button two clicked")