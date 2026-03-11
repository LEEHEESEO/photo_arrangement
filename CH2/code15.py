import os
import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow
)

basedir = os.path.dirname(__file__)
print("current working folder : ", os.getcwd())
print("path are relative to   : ", basedir)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")
        
        widget = QLabel("Hello")
        widget.setPixmap(QPixmap(os.path.join(os.path.dirname(__file__), "pic.jpg")))
        widget.setScaledContents(True)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

#
# 
# 위 코드 중
# basedir = os.path.dirname(__file__)
# print("current working folder : ", os.getcwd())
# print("path are relative to   : ", basedir)
# 에 대해서 설명해줘 
# #