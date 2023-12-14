import sys
import sqlite3

from PyQt5 import uic
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QInputDialog, QMainWindow


class Slide:
    '''Формирурет диалоговое окно'''

    def __init__(self, text):
        # self.text = text
        self.dialog = QInputDialog

    def draw_screen(self):
        self.label = QtWidgets.QLabel()
        self.label.setGeometry(QtCore.QRect(141, 20, 190, 80))


class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('welcome1.ui', self)
        self.current_id = 1
        self.pushWelcome.clicked.connect(self.get_result)
        self.text_screen = ''
        self.text_choices = []
        self.con = sqlite3.connect('project.sqlite')

    def get_result(self):
        '''"Вытаскивает" нужный текст из таблицы'''
        cur = self.con.cursor()
        self.text_screen = cur.execute("""SELECT text FROM Screens
        WHERE id = ?""", (self.current_id,)).fetchone()[0]
        # text_choices = cur.execute("""SELECT text FROM Choices
        # WHERE Choices.screen_id == Screens.id""").fetchall()
        self.slide_text.setText(self.text_screen)
        self.text_choices = cur.execute("""SELECT text FROM Choices
        WHERE screen_id = ?""", (self.current_id,)).fetchall()
        self.text_choices = list(map(lambda x: x[0], self.text_choices))
        self.pushWelcome.setText('Продолжить')
        self.pushWelcome.clicked.connect(self.write)

    def write(self):
        '''Записывает текст в диалоговое окно'''
        text, ok_pressed = QInputDialog().getText(self, "Введите имя", *self.text_choices)
        if ok_pressed:
            if self.correct_answer():
                self.textBrowser.setText(self.text_screen)

    def correct_answer(self):
        '''Проверяет правильность ответов в задачах со счетом'''
        cur = self.con.cursor()
        print(self.current_id)
        correct = cur.execute("""SELECT answer FROM Answers 
        WHERE id = ?""", (self.current_id,)).fetchone()[0]
        if self.text != correct:
            self.textBrowser.setText('Возможно, Вы промазали по нужной клавише. Попытайтесь ещё раз')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = Game()
    ex.show()
    sys.exit(app.exec())
