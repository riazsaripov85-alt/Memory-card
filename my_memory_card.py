from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QTextEdit, QVBoxLayout, QHBoxLayout, QRadioButton


app = QApplication([])
main_win = QWidget()
main_win.show()
b1 = QRadioButton()
b2 = QRadioButton()
b3 = QRadioButton()
b4 = QRadioButton()

b5 = QPushButton()

t1=QLabel("😀😀😀")
t2=QLabel("😎😋😍")

b6=QPushButton()


b7=QPushButton()

b8 = QRadioButton()
b9 = QRadioButton()
b10 = QRadioButton()
b11 = QRadioButton()

t3=QLabel("🤣😂🤣")

h1=QHBoxLayout()
h1.addWidget(b1)
h1.addWidget(b2)
h1.addWidget(b3)
h1.addWidget(b4)
''' ПОТОМ ЧТОБЫ БОЛЬШУЮ ГОРИЗОНТАЛЬ СДЕЛАТЬ ЧЕРЕЗ ADDLAYOUT ОБЪЯВИТЬ'''
v1 = QVBoxLayout()
v1.addLayout(h1)
v1.addWidget(b5)
v1.addWidget(t1)
v1.addWidget(t2)
v1.addWidget(b6)

v2 = QVBoxLayout()
v2.addWidget(b7)

v2.addWidget(b8)
v2.addWidget(b9)
v2.addWidget(b10)
v2.addWidget(b11)

v2.addWidget(t3)

h2=QHBoxLayout()

h2.addLayout(v1)
h2.addLayout(v2)




main_win.setLayout(h2)


app.exec_()