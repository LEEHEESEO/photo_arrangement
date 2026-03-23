import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QLabel,
    QStatusBar,
    QToolBar
)
from PyQt6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("code 39")
        
        label = QLabel("hello")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)
        
        toolbar = QToolBar("My Main ToolBar")
        self.addToolBar(toolbar)
        
        button_action = QAction("your button", self)
        button_action.setStatusTip("this is button for your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)
        
        self.setStatusBar(QStatusBar(self))
        
    def onMyToolBarButtonClick(self, s):
        print("clicked!! %s" %(s))
        
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()