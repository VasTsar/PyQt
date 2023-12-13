import sys
import sqlite3

from PyQt5 import uic
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QInputDialog, QMainWindow


class Slide:
    def __init__(self):
        self.text = input()
        self.dialog = QInputDialog


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
        self.slide_text.setText(self.text_screen)
        self.text_choices = cur.execute("""SELECT text FROM Choices
        WHERE screen_id = ?""", (self.current_id,)).fetchall()
        self.text_choices = list(map(lambda x: x[0], self.text_choices))
        self.pushWelcome.setText('Продолжить')
        self.pushWelcome.clicked.connect(self.write)

    def correct_answer(self):
        '''Проверяет правильность ответов в задачах со счетом'''
        cur = self.con.cursor()
        correct = cur.execute("""SELECT answer FROM Answers 
        WHERE id = ?""", (self.current_id,)).fetchone()[0]
        if self.text == '' or self.text != correct:
            self.textBrowser.setText('Возможно, Вы промазали по нужной клавише. Попытайтесь ещё раз')

    def write(self):
        '''Записывает текст в диалоговое окно'''
        cur = self.con.cursor()
        text, ok_pressed = QInputDialog().getText(self, "Введите имя", *self.text_choices)
        type_choice = cur.execute("""SELECT type_choice FROM Choices
        WHERE id = ?""", (self.current_id,)).fetchone()[0]
        if ok_pressed:
            if type_choice == 'input':
                self.correct_answer()
                self.textBrowser.setText(self.text_screen)

    def correct_answer(self):
        '''Проверяет правильность ответов в задачах со счетом'''
        cur = self.con.cursor()
        print(self.current_id)
        correct = cur.execute("""SELECT answer FROM Answers 
        WHERE id = ?""", (self.current_id,)).fetchone()[0]
        if self.text != correct:
            self.textBrowser.setText('Возможно, Вы промазали по нужной клавише. Попытайтесь ещё раз')

    def insert_statistics(self):
        '''Добавляет номер игрока, время и концовку в таблицу'''
        statistics_insert_statistics = '''INSERT INTO Statistics (time,end) VALUES(time_, end_)'''
        # time_ - время / end_ - номер концовки


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = Game()
    ex.show()
    sys.exit(app.exec())
