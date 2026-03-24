import sys
import os
from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QToolBar,
    QStatusBar,
    QCheckBox,
)

basedir = os.path.dirname(__file__)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CODE 45")
        
        label = QLabel("CODE 45")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)
        
        toolbar = QToolBar("Main ToolBar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)
        
        b1 = QAction(
            QIcon(os.path.join(basedir, "bug.png")),
            "button 1",
            self
        )
        b1.setStatusTip("the first button")
        b1.triggered.connect(self.onMyToolBarButtonClick)
        b1.setCheckable(True)
        b1.setShortcut(QKeySequence("Ctrl+p"))
        toolbar.addAction(b1)
        toolbar.addSeparator()
        
        b2 = QAction(
            QIcon(os.path.join(basedir, "bug.png")),
            "button2",
            self
        )
        b2.setStatusTip("the second button")
        b2.triggered.connect(self.onMyToolBarButtonClick)
        b2.setCheckable(True)
        toolbar.addAction(b2)
        toolbar.addSeparator()
        
        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())
        
        self.setStatusBar(QStatusBar())
        
        menu = self.menuBar()
        
        file_menu = menu.addMenu("file")
        file_menu.addAction(b1)
        file_menu.addSeparator()
        
        file_submenu = file_menu.addMenu("Sub menu")
        file_submenu.addAction(b2)
        
    def onMyToolBarButtonClick(self, s):
        print(s)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()