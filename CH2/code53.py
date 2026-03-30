import sys
from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow,
    QMessageBox,
    QPushButton
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Code 53")
        
        button = QPushButton("press")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)
        
    def button_clicked(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I havea question!!")
        dlg.setText("this is a question dialog")
        dlg.setStandardButtons(
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        dlg.setIcon(QMessageBox.Icon.Question)
        
        button = dlg.exec()
        
        button = QMessageBox.StandardButton(button)
        
        if button == QMessageBox.StandardButton.Yes:
            print("yes!!")
        else:
            print("no!")
            
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()