import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QPushButton
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Code54")
        
        button = QPushButton("press")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)
        
    def button_clicked(self, s):
        button = QMessageBox.question(
            self, 
            "Question Dialog", 
            "The longer message"
        )
        
        if button == QMessageBox.StandardButton.Yes:
            print("yes")
        else :
            print("no")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()