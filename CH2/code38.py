import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QToolBar,
    QStatusBar
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("code 38")
        
        label = QLabel("Hello!!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)
        
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)
        
        button_action = QAction("your button", self)
        button_action.setStatusTip("the buttons")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action)
        
        self.setStatusBar(QStatusBar(self))
        
    def onMyToolBarButtonClick(self, s):
        print("click %s" %(s))
        
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()