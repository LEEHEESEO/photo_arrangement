import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QToolBar,
    QLabel,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("code 37")
        
        label = QLabel("My Main ToolBar")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)
        
        toolbar = QToolBar("My Main Toolbar")
        self.addToolBar(toolbar)
        
        button_action = QAction("your button", self)
        button_action.setStatusTip("this is your button")
        button_action.triggered.connect(self.onMyToolBarButton)
        toolbar.addAction(button_action)
        
    def onMyToolBarButton(self, s):
        print("click %s" %(s))
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()