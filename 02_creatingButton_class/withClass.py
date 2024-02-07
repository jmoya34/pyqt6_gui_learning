# Using OOP
from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow
import sys


# Adding content to window using a subclass  to customize 
class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Holder app")
        button = QPushButton("Press Me!")

        #locate the button
        self.setCentralWidget(button)



app = QApplication(sys.argv)
window = ButtonHolder() # 
window.show() 
app.exec() 