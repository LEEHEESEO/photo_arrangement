import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("my app")
        
        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText("Enter Your Text")
        
        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)
        
        self.setCentralWidget(widget)
        
    def return_pressed(self):
        print("return pressed")
        self.centralWidget().setText("BOOM")
    def selection_changed(self):
        print("selection changed")
        print(self.centralWidget().selectedText())
    def text_changed(self, s):
        print("Text Changed . . .")
        print(s)
    def text_edited(self, s):
        print("Text Edited . . .")
        print(s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()        