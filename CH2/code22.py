import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QSlider
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("my app")
        
        widget = QSlider()
        
        
        widget.setMinimum(-10)
        widget.setMaximum(10)
        widget.setSingleStep(1)
        
        widget.valueChanged.connect(self.value_changed)
        
        widget.sliderMoved.connect(self.slider_moved)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)
        
        self.setCentralWidget(widget)
        
    def value_changed(self, value):
        print(value)
        
    def slider_moved(self, postion):
        print("postion --> %s" %(postion))
    def slider_pressed(self):
        print("slider pressed")
    def slider_released(self):
        print("slider released")
        
    
app = QApplication(sys.argv)

window= MainWindow()
window.show()

app.exec()