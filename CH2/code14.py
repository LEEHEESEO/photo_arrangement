import sys
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import(
    QMainWindow,
    QApplication,
    QLabel
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("라벨에 사진 올리기")
        
        widget = QLabel("Hello")
        widget.setPixmap(QPixmap("C:/Users/ranso/OneDrive/바탕 화면/KakaoTalk_20260312_001913087.jpg"))
        
        self.setCentralWidget(widget)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()