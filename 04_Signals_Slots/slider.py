from PySide6.QtWidgets import QApplication, QSlider
from PySide6.QtCore import Qt

# The slot
def slider_response(data):
    print("Slider location:", data)

app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

# Signal
slider.valueChanged.connect(slider_response)

# Begin gui
slider.show()
app.exec()