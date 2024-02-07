from PySide6.QtWidgets import QPushButton, QMainWindow

# Adding content to window using a subclass  to customize 
class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Holder app")
        button = QPushButton("Press Me!")

        #locate the button
        self.setCentralWidget(button)