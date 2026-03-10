from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton
)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")
        
        button = QPushButton("Press")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        
        self.setCentralWidget(button)
    
    def the_button_was_clicked(self):
        print("clicked")
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()