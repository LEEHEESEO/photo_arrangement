import sys
from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow,
    QPushButton,
)
from code50 import CustomDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CODE 47")
        
        button = QPushButton("PRESS ME FOR A DIALOG")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)
        
    def button_clicked(self, s):
        print("clicked %s" %(s))
        
        dlg = CustomDialog(self)
        if dlg.exec():
            print("success!")
        else:
            print("cancel")
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()