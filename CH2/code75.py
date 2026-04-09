import sys
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget
)

class AnotherWindow(QWidget):
    """
        이 윈도우는 QWidget이다. 부모가 없는 경우, 자유롭게 떠 있는 윈도우로 나타난다. 
    """
    
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CODE 75")
        
        self.button = QPushButton("New Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)
        
    def show_new_window(self, checked):
        self.w = AnotherWindow()
        self.w.show()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

#show_new_window() 에서 w에 self.를 붙여주지 않으면 윈도우가 1초 미만으로 나타났다가 사라져.
#self를 붙이면 문제가 해결되는데, 책에서는 '기본 윈도우 자체 객체에서 윈도우에 대한 참조를 어딘가에 보관해야 한다'라고 돼 있는데,
# 이건 w를  MainWindow()에 참조한다는건가? 참조라는건 데이터에 대한 정보를 메모리 안에 저장해놓고 그 메모리에 직접 접근하는 것을 통해
# 데이터를 사용하는 거잖아? 변수에 self를 붙이는 것으로 참조를 한다는게 무슨 말인지 모르겠어. 