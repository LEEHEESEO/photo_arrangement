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
        self.setWindowTitle("CODE 55")
        
        button = QPushButton("press")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)
        
    def button_clicked(self, s):
        buttons = (
            QMessageBox.StandardButton.Discard |
            QMessageBox.StandardButton.NoToAll |
            QMessageBox.StandardButton.Ignore
        )
        
        button = QMessageBox.critical(
            self,
            "Oh dear",
            "something went wrong!",
            buttons,
            defaultButton = QMessageBox.StandardButton.Discard
        )
        
        if button == QMessageBox.StandardButton.Discard:
            print("Discard!")
        elif button == QMessageBox.StandardButton.NoToAll:
            print("NoToAll")
        else :
            print("Ingore")
            
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()