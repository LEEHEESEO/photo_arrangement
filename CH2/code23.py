import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QDial
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("code 23")
        
        widget = QDial()
        widget.setRange(-10, 100)
        widget.setSingleStep(5)
        
        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)
        
        self.setCentralWidget(widget)
        
    def value_changed(self, value):
        print("value --> %s" %(value))
    def slider_position(self, position):
        print("current position --> %s" %(position))
    def slider_pressed(self):
        print("slier pressed")
    def slider_released(self):
        print("slier_released")
        
    
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()        
        