import sys
from PyQt6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

window = QPushButton("Push Me")
# push 버튼 하나만 존재하는 윈도우 
window.show()

app.exec()