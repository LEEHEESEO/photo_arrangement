import os
import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QToolBar,
    QStatusBar,
    QCheckBox
)

basedir = os.path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("code 42")
        
        label = QLabel("hello!!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)
        
        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)
        
        button1 = QAction(
            QIcon(os.path.join(basedir, "bug.png")),
            "button1",
            self
        )
        button1.setStatusTip("first button")
        button1.setCheckable(True)
        button1.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button1)
        
        toolbar.addSeparator()
        
        button2 = QAction(
            QIcon(os.path.join(basedir, "bug.png")),
            "button2",
            self
        )
        button2.setStatusTip("second button")
        button2.setCheckable(True)
        button2.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button2)
        toolbar.addSeparator()
        
        toolbar.addWidget(QLabel("hello"))
        toolbar.addWidget(QCheckBox())
        
        self.setStatusBar(QStatusBar(self))
        
        menu = self.menuBar()
        
        file_menu = menu.addMenu("File")
        file_menu.addAction(button1)
        
    def onMyToolBarButtonClick(self, s):
        if s:
            print("clicked")
        else:
            print("unclicked")
            
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
        