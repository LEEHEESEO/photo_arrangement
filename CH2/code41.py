import os
import sys
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QStatusBar,
    QToolBar,
    QCheckBox
)

basedir = os.path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("code 41")
        
        label = QLabel("hello")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)
        
        toolbar = QToolBar("button")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)
        
        button_action = QAction(
            QIcon(os.path.join(basedir, "bug.png")),
            "bug button",
            self
        )
        button_action.setStatusTip("debugging button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        
        toolbar.addAction(button_action)
        toolbar.addSeparator()
        
        button_action2 = QAction(
            QIcon(os.path.join(basedir, "bug.png")),
            "bug button 2",
            self
        )
        button_action2.setStatusTip("debugging button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        
        toolbar.addAction(button_action2)
        toolbar.addAction(button_action2)
        
        toolbar.addWidget(QLabel("hello"))
        toolbar.addWidget(QCheckBox())
        
        self.setStatusBar(QStatusBar(self))
    
    def onMyToolBarButtonClick(self, s):
        if s:
            print("clicked")
        else:
            print("unclicked")
            
    
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()