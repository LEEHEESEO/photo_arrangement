import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QInputDialog,
    QLineEdit
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Code 57")
        
        layout = QVBoxLayout()
        
        button1 = QPushButton("Integer")
        button1.clicked.connect(self.get_an_int)
        layout.addWidget(button1)
        
        button2 = QPushButton("Float")
        button2.clicked.connect(self.get_a_float)
        layout.addWidget(button2)
        
        button3 = QPushButton("Select")
        button3.clicked.connect(self.get_a_str_from_a_list)
        layout.addWidget(button3)
        
        button4 = QPushButton("String")
        button4.clicked.connect(self.get_a_str)
        layout.addWidget(button4)
        
        button5 = QPushButton("Text")
        button5.clicked.connect(self.get_text)
        layout.addWidget(button5)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
    def get_an_int(self):
        title = "Enter an integer"
        label = "Type your integer here"
        my_int_value, ok = QInputDialog.getInt(
            self,
            title,
            label,
            value = 0,
            min = -5,
            max = 5,
            step = 1
        )
        print(f"Result : {my_int_value}, {ok}")
        
    def get_a_float(self):
        title = "Enter a float"
        label = "Type your float here"
        my_float_value, ok = QInputDialog.getDouble(
            self,
            title,
            label,
            value = 0,
            min = -5.3,
            max = 5.7,
            decimals = 2
        )
        print(f"Result : {my_float_value}, {ok}")
        
    def get_a_str_from_a_list(self):
        title = "Select a string"
    
    def get_a_str(self):
        pass
    def get_text(self):
        pass
        
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
        
#Decimals 는 무슨 변수야?