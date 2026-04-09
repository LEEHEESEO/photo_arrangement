import sys
from random import randint
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget
)

class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        label = QLabel("The number is %s" %(randint(0, 100)))
        layout.addWidget(label)
        self.setLayout(layout)
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CODE 81")
        
        self.w = AnotherWindow()
        self.button = QPushButton("push for a new window")
        self.button.clicked.connect(self.open_new_window)
        self.setCentralWidget(self.button)
        
    def open_new_window(self, checked):
        self.w.show()
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()