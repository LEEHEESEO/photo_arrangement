import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        
        button = QPushButton("Press Me")
        
        self.setFixedSize(QSize(400,300))
        # 윈도우의 크기를 고정시킨다.
        # 즉 사용자가 윈도우의 크기를 임의로 조정할 수 없게 된다. 
        self.setCentralWidget(button)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()