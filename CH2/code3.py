from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)

window = QMainWindow()
# QMainWindow는 사용자를 위한 표준 윈도우 기능을 제공한다. 
window.show()

app.exec()