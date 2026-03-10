from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton
)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.button_is_chekced = True
        self.setWindowTitle("my app")
        
        button = QPushButton("Press")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_toggled)
        button.setChecked(self.button_is_chekced)
        
        self.setCentralWidget(button)
        
    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print(self.button_is_checked)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

# 이 코드에서 button.setChecked(self.button_is_chekced) 는 무슨 역할을 하는거야? 
# setChecked라는 함수의 기능과 함께 설명해줘