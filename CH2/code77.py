from random import randint
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QWidget
)

class AnotherWindow(QWidget):
    """
    """
    
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window %d" %(randint(0, 100)))
        layout.addWidget(self.label)
        self.setLayout(layout)
    

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CODE 76")
        
        button = QPushButton("Open New Window")
        button.clicked.connect(self.open_new_window)
        self.setCentralWidget(button)
        
    def open_new_window(self, checked):
        self.w = AnotherWindow()
        self.w.show()
    
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()