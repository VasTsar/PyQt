import sys
import sqlite3

from PyQt5 import uic
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QInputDialog, QMainWindow
from datetime import datetime


class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('welcome1.ui', self)
        self.current_id = 1
        self.pushWelcome.clicked.connect(self.get_result)
        self.text_screen = ''
        self.text_choices = []
        self.con = sqlite3.connect('project.sqlite')
        #self.start_time = datetime.now.time()

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

    def write(self):
        '''Записывает текст в диалоговое окно'''
        '''cur = self.con.cursor()
        text, ok_pressed = QInputDialog().getInt(self, "Введите имя", *self.text_choices)
        if ok_pressed:
            self.textBrowser.setText(self.text_screen)'''

    def insert_statistics(self):
        '''Добавляет номер игрока, время и концовку в таблицу'''
        #self.time_ = datetime.now().time - self.start_time
        statistics_insert_statistics = '''INSERT INTO Statistics (time,end) VALUES(self.time_, self.end_)'''
        # time_ - время / end_ - номер концовки


class Slide(Game):
    def __init__(self, parent=None, text_choices=None, text_screen=None, end1='final1.png', end2='final2.png'):
        super().__init__(parent)
        uic.loadUi('dialog.ui', self)
        self.label.setText(self.text_screen)
        self.PushButton_1.set.Text(self.text_choices[0])
        self.PushButton_2.set.Text(self.text_choices[1])

        # self.pixmap = QPixmap(image)
        # self.label.setPixmap(self.pixmap)

    def draw_screen(self):
        '''Рисует экран'''
        pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = Game()
    ex.show()
    sys.exit(app.exec())
