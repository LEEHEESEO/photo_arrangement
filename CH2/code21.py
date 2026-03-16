import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QSpinBox,
    QDoubleSpinBox
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("오늘 마지막 코드!!")
        
        widget = QSpinBox()
        widget.setRange(-10,10)
        
        widget.setPrefix("$")
        widget.setSuffix("c")
        widget.setSingleStep(1)
        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(self.text_changed)
        
        self.setCentralWidget(widget)
        
    def value_changed(self, v):
        print("value changed")
        print(v)
    def text_changed(self, t):
        print("text changed")
        print(t)
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()