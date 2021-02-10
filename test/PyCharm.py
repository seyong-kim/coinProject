# ch03/03_12.py
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pykorbit

form_class = uic.loadUiType("myWindow.ui")[0]

class MyWindow(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.display.clicked.connect(self.inquiry)
        self.setWindowTitle('Hello')
        # self.setGeometry(100, 200, 300, 400)
        # self.setWindowTitle('Hello')
        # # self.setWindowIcon(QIcon("icon.png"))

        # btn1 = QPushButton("버튼1", self)
        # btn1.move(10, 10)
        # btn1.clicked.connect(self.btn_clicked)

        # btn2 = QPushButton("버튼2", self)
        # btn2.move(10, 40)
        # btn2.clicked.connect(self.btn_clicked)

    def inquiry(self) :
        price = pykorbit.get_current_price('BTC')
        print(price)
        self.lineEdit.setText(str(price))

app = QApplication(sys.argv)         # QApplication 객체 생성

# label = QLabel("Hello")
# label.show()

# btn = QPushButton("Hello")
# btn.show()

window = MyWindow()
window.show()

app.exec_()                          # 이벤트 루프 생성