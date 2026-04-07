import sys, os
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QFileDialog
)

basedir = os.path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CODE 65")
        
        button = QPushButton("OPEN FILE")
        button.clicked.connect(self.get_filename)
        
        self.setCentralWidget(button)
        
    def get_filename(self):
        filters = "Portable Networ Graphics files (*.png);;Python Code files (*.py);;All files(*.)"
        print("Filters are:", filters)
        filename, selected_filter = QFileDialog.getOpenFileName(self, "File Opened", basedir, filter=filters)
        print("Result : ", filename, selected_filter)
    
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()