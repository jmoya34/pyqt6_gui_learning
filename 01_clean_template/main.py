### Take Note that this script contains everything in global scope

from PySide6.QtWidgets import QApplication, QWidget

# This is to processing command lines arguments
import sys

# Runs application and runs the events
app = QApplication(sys.argv)

window = QWidget()
window.show() # starts the window

app.exec() # Starts the event loop that waits for events to occur