import sys
import os
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QToolBar,
    QCheckBox,
    QStatusBar,
)

basedir = os.path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("code 43")
        
        label = QLabel("CODE 43")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)
        
        toolbar = QToolBar("Main ToolBar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)
        
        button1 = QAction(
            QIcon(os.path.join(basedir, "bug.png")),
            "button1",
            self
        )
        button1.setStatusTip("the first action")
        button1.setCheckable(True)
        button1.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button1)
        
        toolbar.addSeparator()
        
        button2 = QAction(
            QIcon(os.path.join(basedir, "bug.png")),
            "button2",
            self
        )
        button2.setCheckable(True)
        button2.setStatusTip("the second action")
        button2.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button2)
        
        toolbar.addSeparator()
        
        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())
        
        self.setStatusBar(QStatusBar())
        
        menu = self.menuBar()
        file_menu = menu.addMenu("File")
        
        file_menu.addAction(button1)
        file_menu.addSeparator()
        file_menu.addAction(button2)
        
    def onMyToolBarButtonClick(self, s):
        print(s)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
        