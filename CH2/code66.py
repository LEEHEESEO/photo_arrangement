import sys, os
from PyQt6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QPushButton
)

basedir = os.path.dirname(__file__)

FILE_FILTERS = [
    "Portable Network Graphics files (*.png)",
    "Text files (*.txt)",
    "Pytoh Source files (*.py)",
    "Comma Separated Values (*.csv)",
    "All files (*.*)"
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CODE 66")
        
        button = QPushButton("OPEN FILE")
        button.clicked.connect(self.get_filename)

        self.setCentralWidget(button)
        
    def get_filename(self):
        initial_filter = FILE_FILTERS[0]
        filters = ";;".join(FILE_FILTERS)
        print("Filters are: ", filters)
        print("Inital filter:", initial_filter)
        
        filename, selected_filter = QFileDialog.getOpenFileName(
            self,
            "open File",
            basedir,
            filter = filters,
            initialFilter = initial_filter
        )
        print(f"result --> {filename}, {selected_filter}")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

# 질문 1 : QFileDialog.getOpenFileName()이 받는 initialFilter은 어떤 작업을 위한 파라미터야?
# 질문 2 : 열고자 하는 파일 위치가 QFileDialog.getOpenFileName()의 세 번째 인자로 전달되는데, 세 번째 인자로 전달 되게 하는 것이 아닌
# 파라미터 순서에 무관하게 전달되게 하려면 어떻게 해야 해?