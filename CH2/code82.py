import sys
from random import randint
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget
)

class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("number --> %s" %(randint(0,100)))
        layout.addWidget(label)
        
        self.setLayout(layout)
        
    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = AnotherWindow()
        
        self.button = QPushButton("open a new window")
        self.button.clicked.connect(self.open_window)
        self.setCentralWidget(self.button)
        
    def open_window(self, checked):
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()