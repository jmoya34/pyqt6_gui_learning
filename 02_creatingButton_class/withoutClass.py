# No organization
from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow
import sys

app = QApplication(sys.argv)
window = QMainWindow() # base class

# Adding content to window
window.setWindowTitle("Hello World") # Slots type in docmentation 

button = QPushButton() # Call to 
button.setText("Press me") # setText is a constructor used to change the label

window.setCentralWidget(button) # There is no setCentralWidget attribute in documentation and throws an error

# begining window routine
window.show() 
app.exec() 