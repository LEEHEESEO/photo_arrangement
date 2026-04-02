import sys
from PyQt6.QtWidgets import (
    QApplication,
    QInputDialog,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QWidget,
    QVBoxLayout
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        
        layout = QVBoxLayout()
        
        button1 = QPushButton("Integer")
        button1.clicked.connect(self.get_an_int)
        layout.addWidget(button1)
        
        button2 = QPushButton("Float")
        button2.clicked.connect(self.get_a_float)
        layout.addWidget(button2)
        
        button3 = QPushButton("Select")
        button3.clicked.connect(self.get_str_from_list)
        layout.addWidget(button3)
        
        button4 = QPushButton("String")
        button4.clicked.connect(self.get_str)
        layout.addWidget(button4)  
        
        button5 = QPushButton("Text")   
        button5.clicked.connect(self.get_text)
        layout.addWidget(button5)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
    def get_an_int(self):
        dialog = QInputDialog(self)
        dialog.setWindowTitle("Enter an integer")
        dialog.setLabelText("Type your integer here")
        dialog.setIntValue(0)
        dialog.setIntMaximum(10)
        dialog.setIntMinimum(-10)
        dialog.setIntStep(1)
        
        ok = dialog.exec()
        print(f"Result --> {ok}, {dialog.intValue()}")
        
    def get_a_float(self):
        dialog = QInputDialog(self)
        dialog.setWindowTitle("Enter a float here")
        dialog.setLabelText("Type your float here")
        dialog.setDoubleValue(0)
        dialog.setDoubleMaximum(9.8)
        dialog.setDoubleMinimum(-8.9)
        dialog.setDoubleStep(0.1)
        dialog.setDoubleDecimals(2)
        
        ok = dialog.exec()
        print(f"Result --> {ok}, {dialog.doubleValue()}")
        
    def get_str_from_list(self):
        dialog = QInputDialog(self)
        dialog.setWindowTitle("Select a string")
        dialog.setLabelText("Select a fruit from the list")
        dialog.setComboBoxItems(["apple", "pear", "orange", "grape"])
        dialog.setComboBoxEditable(True)
        dialog.setTextValue("orange")
        
        ok = dialog.exec()
        print(f"Result --> {ok}, {dialog.textValue()}")
        
    def get_str(self):
        dialog = QInputDialog(self)
        dialog.setWindowTitle("Enter a string")
        dialog.setLabelText("Type your password")
        dialog.setTextValue("my password")
        dialog.setTextEchoMode(QLineEdit.EchoMode.Password)
        
        ok = dialog.exec()
        print(f"Result --> {ok}, {dialog.textValue()}")
        
    def get_text(self):
        dialog = QInputDialog(self)
        dialog.setWindowTitle("Enter text")
        dialog.setLabelText("Type your novel here")
        dialog.setTextValue("Once upon a time..")
        dialog.setOption(
            QInputDialog.InputDialogOption.UsePlainTextEditForTextInput,True,
        )
        
        ok = dialog.exec()
        print(f"Result --> {ok}, {dialog.textValue()}")
        
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()