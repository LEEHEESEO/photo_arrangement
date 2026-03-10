from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QPushButton
)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("app")
        
        self.button = QPushButton("눌러봐")
        self.button.clicked.connect(self.the_button_was_clicked)
        
        self.setCentralWidget(self.button)
        
    def the_button_was_clicked(self):
        self.button.setText("버튼을 누르셨습니다.")
        self.button.setEnabled(False)
        
        self.setWindowTitle("일회용 앱이었지롱")
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()