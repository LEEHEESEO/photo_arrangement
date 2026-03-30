import sys
from PyQt6.QtWidgets import (
    QApplication,
    QInputDialog,
    QMainWindow,
    QPushButton
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CODE 56")
        
        button1 = QPushButton("press")
        button1.clicked.connect(self.get_an_int)
        
        self.setCentralWidget(button1)
        
    def get_an_int(self):
        my_int_value, ok = QInputDialog.getInt(
            self,
            "get an ingeter",
            "Ender a number"
        )
        print("result %s" %(ok, my_int_value))
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()