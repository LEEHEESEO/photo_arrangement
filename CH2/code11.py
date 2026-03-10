from PyQt6.QtWidgets import(
    QApplication,
    QMainWindow,
    QPushButton
)
from random import choice
import sys

window_title = [
    "My App",
    "My App",
    "Still My App",
    "Still My App",
    "What on Earth",
    "What on Earth",
    "This is Surprising",
    "This is Surprising",
    "Something went wrong"
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.n_times_clicked = 0
        
        self.setWindowTitle("My app")
        
        self.button = QPushButton("press")
        self.button.clicked.connect(self.the_button_was_clicked)
        self.windowTitleChanged.connect(self.the_window_title_changed)
        self.setCentralWidget(self.button)
        
    def the_button_was_clicked(self):
        print("Clicked, so the title will be changed.. or not")
        new_window_title = choice(window_title)
        print("Setting title: %s" % new_window_title)
        self.setWindowTitle(new_window_title)
        
    def the_window_title_changed(self, window_title):
        print("Window title changed to %s" %window_title)
        if window_title == "Something went wrong":
            self.button.setEnabled(False)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()