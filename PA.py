import sys
from pathlib import Path

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 1. 창 기본 설정
        self.setWindowTitle("Photo Arrangement")
        self.setGeometry(300, 300, 400, 200)

        # 2. 드래그 허용 설정
        self.setAcceptDrops(True)

        # 3. 안내 문구 라벨 생성
        self.label = QLabel("폴더를 드래그 하세요")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 4. 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    # 5. 드래그가 들어왔을 때 호출
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    # 6. 드롭했을 때 호출
    def dropEvent(self, event):
        urls = event.mimeData().urls()

        if urls:
            folder_path = urls[0].toLocalFile()
            path = Path(folder_path)

            if path.is_dir():
                self.label.setText(f"선택된 폴더:\n{folder_path}")
                print("폴더 경로:", folder_path)


# 7. 프로그램 실행 부분
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
