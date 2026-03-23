import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QLabel,
    QToolBar
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("code 36")
        
        label = QLabel("hello")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.setCentralWidget(label)
        
        toolbar = QToolBar("My Main toolbar")
        self.addToolBar(toolbar)
        
    def onMyToolBarButtonClick(self, s):
        print("click, ", s)
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()