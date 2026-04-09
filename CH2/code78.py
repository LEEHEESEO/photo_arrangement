import sys
from random import randint
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QWidget,
    QVBoxLayout
)

class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        label = QLabel("This time, the number is %s" %(randint(0,100)))
        layout.addWidget(label)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CODE 78")
        
        self.w = None
        button = QPushButton("Opne a new Window")
        button.clicked.connect(self.open_new_window)
        self.setCentralWidget(button)
        
    def open_new_window(self, check):
        if self.w is None:
            self.w = AnotherWindow()
            self.w.show()
        else :
            self.w.close()
            self.w = None
            
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()