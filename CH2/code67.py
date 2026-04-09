import sys, os
from PyQt6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QMessageBox
)

basedir = os.path.dirname(__file__)
FILE_FILTERS = [
    "Poratable Network Graphics files (*.png)",
    "Text files (*.txt)",
    "Python files (*.py)",
    "Comma Separated Values (*.csv)",
    "All files (*)"
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CODE 67")
        
        layout = QVBoxLayout()
        
        button1 = QPushButton("Open File")
        button1.clicked.connect(self.get_filename)
        layout.addWidget(button1)
        
        button2 = QPushButton("Open Files")
        button2.clicked.connect(self.get_filenames)
        layout.addWidget(button2)
        
        button3 = QPushButton("Save file")
        button3.clicked.connect(self.get_save_filename)
        layout.addWidget(button3)
        
        button4 = QPushButton("Select folder")
        button4.clicked.connect(self.get_folder)
        layout.addWidget(button4)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
    def get_filename(self):
        initial_filter = FILE_FILTERS[4]
        filters = ";;".join(FILE_FILTERS)
        print("Filters are:", filters)
        print("Initial Filter is:", initial_filter)
        
        filename, selected_filter = QFileDialog.getOpenFileName(
            self,
            directory=basedir,
            filter = filters,
            initialFilter=initial_filter
        )
        print(f"Result: {filename}, {selected_filter}")
        
        if filename:
            os.startfile(filename)
    
    def get_filenames(self):
        caption = "데이터 파일을 모두 선택하세요"
        initial_dir = ""
        initial_filter = FILE_FILTERS[4]
        filters = ";;".join(FILE_FILTERS)
        print("Filters are:", filters)
        print("Initial filter:", initial_filter)
        
        filename, selected_filter = QFileDialog.getOpenFileNames(
            self,
            directory = basedir,
            caption = caption,
            filter = filters,
            initialFilter=initial_filter
        )
        print(f"Result: {filename}, {selected_filter}")
        
    def get_save_filename(self):
        caption = "get save filenames"
        initial_dir = ""
        initial_filter = FILE_FILTERS[4]
        filters = ";;".join(FILE_FILTERS)
        print("Filters are : %s" %(filters))
        print("Initial Filter : %s" %(initial_filter))
        
        filename, selected_filter = QFileDialog.getSaveFileName(
            self,
            caption = caption,
            directory = basedir,
            initialFilter = initial_filter,
            filter = filters
        )
        print(f"Result: {filename}, {selected_filter}")
        if filename:
            if os.path.exists(filename):
                write_confirmed = QMessageBox.question(
                    self,
                    "덮어쓰기",
                    f"{filename}은 이미 존재하는 파일입니다. 덮어쓰시겠습니까?"
                )
            else :
                write_confirmed = True
        
        if write_confirmed:
            with open(filename, "w") as f:
                file_content = "YOUR FILE CONTENT"
                f.write(file_content)
                
        
    def get_folder(self):
        caption = "select folder"
        initial_dir = basedir
        initial_filter = FILE_FILTERS[1]
        
        dialog = QFileDialog()
        dialog.setWindowTitle(caption)
        dialog.setDirectory(initial_dir)
        dialog.setNameFilters(FILE_FILTERS)
        dialog.selectNameFilter(initial_filter)
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        
        ok = dialog.exec()
        print(
            "Result", ok, dialog.selectedFiles(), dialog.selectedNameFilter()
        )
        
    

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

###
#if filename:
#            with open(filename, "r") as f:
#                file_contents = f.read()
 #   이 코드가 있는데도 get_filename이 호출됐을 때 파일이 열리지 않는 이유는 무엇일까?
### 