import sys
from math import sin, cos, pi
from random import randint

from PyQt5 import uic
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QInputDialog


'''class Slide:
    def __init__(self):
        self.text = text
        self.dialog = QInputDialog'''


class Welcome(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('welcome1.ui', self)
        self.start_game()

    def start_game(self):
        self.pushWelcome.clicked.connect(self.new_game)
        self.pushWelcome.clicked.connect(self.game1)
        # self.pushWelcome.clicked.connect()

    def setupUi(self, Form):
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(141, 20, 190, 80))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def new_game(self):
        name, ok_pressed = QInputDialog.getText(self, "Введите имя",
                                                "Как Вас называть?")
        if ok_pressed:
            self.pushWelcome.setText('Продолжить')
            self.textBrowser.setText(f'Приятно познакомиться, {name}! Помнить себя очень важно.')

    def game1(self):
        self.textBrowser.setText(f'Вы помните своё имя, уже неплохо. Теперь необходимо подумать о других '
                                 'базовых умениях. Вдруг Вам срочно понадобиться сосчитать, сколько пальцев Вы видите?')

        name, ok_pressed = QInputDialog.getInt(self, "Решите пример",
                                                "Сколько будет 73 - 63?")
        if ok_pressed == '10':
            self.textBrowser.setText(f'Браво! Вы почти великий ученый.')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = Welcome()
    ex.show()
    sys.exit(app.exec())