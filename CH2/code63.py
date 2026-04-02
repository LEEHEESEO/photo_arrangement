import os
basedir = os.path.dirname(__file__)
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QPushButton
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CODE 63")
        
        button1 = QPushButton("Open File")
        button1.clicked.connect(self.get_filename)
        
        self.setCentralWidget(button1)
        
    def get_filename(self):
        filename, selected_filter = QFileDialog.getOpenFileName(self, "Open", basedir)
        print(f"Result --> {filename}, {selected_filter}")
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

#QFileDialog.getOpenFileName()이 반환하는 값 두개와 그 작동에 대해 자세히 설명해줘.
#어떤 원리로 해당 파일을 여는 것인지, 파일을 여는 것은 실행 파일이 있는 곳의 위치인지 아니면 실행하고 있느 곳의 위치인지도 알려줘
#나는 현재 user/PA/ch2/code63.py 에서 작업하고 있는데, 코드를 실행하면 PA가 열리거든. 해당 함수가 어떻게 이 위치를 찾아서 여는 것인지 궁금해