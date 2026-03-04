from PyQt6.QtWidgets import QApplication, QWidget
#PyQt6의 QtWidgets로부터 QApplication과 QWiget이라는 모듈을 받아온다
import sys
# sys는 해당 프로그램의 제어권에 관련된 요소들을 개발자의 컨트롤 아래에 두게 만드는
# 파이썬 내장 모듈이다. 

app = QApplication(sys.argv)
# app 이라는 QApplication의 객체에 프로그램 사용자의 입력값들을 넘겨주어
# 프로그램이 그 입력값들을 받을 수 있도록 한다. 
# 즉 프로그램이 유저와 상호작용 할 수 있도록 만들어준다. 

window = QWidget()
# QWidget 객체 생성
window.show()
# QWidget 실행

app.exec()
# app의 이벤트 루트를 실행한다. 