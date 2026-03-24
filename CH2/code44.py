import os
import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QAction
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
        self.setWindowTitle("CODE 44")
        
        label = QLabel("CODE 44")
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
        button1.setCheckable(True)
        button1.triggered.connect(self.onMyToolBarButtonClick)
        button1.setStatusTip("the first button")
        toolbar.addAction(button1)
        toolbar.addSeparator()
        
        button2 = QAction(
            QIcon(os.path.join(basedir, "bug.png")),
            "button2",
            self
        )
        button2.setCheckable(True)
        button2.triggered.connect(self.onMyToolBarButtonClick)
        button2.setStatusTip("the second button")
        toolbar.addAction(button2)
        toolbar.addSeparator()
        
        toolbar.addWidget(QLabel("외모 췤"))
        toolbar.addWidget(QCheckBox())
        
        self.setStatusBar(QStatusBar(self))
        
        menu = self.menuBar()
        
        file_menu = menu.addMenu("File")
        file_menu.addAction(button1)
        file_menu.addSeparator()
        
        file_submenu = file_menu.addMenu("SubFile")
        file_submenu.addAction(button2)
        
    def onMyToolBarButtonClick(self, s):
        print(s)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()