"""
Signals and Slots are things QT provides to connect things between two pieces of codes
ex) Say a button is pressed, it will send a message to another aspect of the gui to make a response

"""

from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow

# The slot
def button_clicked(data):
    print("Event happened aka button pressed:", data)

app = QApplication()
button = QPushButton("Press me")

# This allows for a toggle for the button to switch between true and false. This would affect the function
button.setCheckable(True)

# Signal would be emitted once the button is clicked
# Wiring a signal and slot is done by line 18
button.clicked.connect(button_clicked)

button.show()
app.exec()
