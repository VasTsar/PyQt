import sys
import sqlite3

from PyQt5 import uic
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QInputDialog, QMainWindow


class Slide:
    def __init__(self, text):
        self.text = text
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

    def get_result(self):
        con = sqlite3.connect('project')
        cur = con.cursor()
        text_screen = cur.execute("""SELECT text FROM Screens
        WHERE id = ?""", (self.current_id,)).fetchone()[0]
        #text_choices = cur.execute("""SELECT text FROM Choices
        #WHERE Choices.screen_id == Screens.id""").fetchall()
        self.slide_text.setText(text_screen)
        text_choices = cur.execute("""SELECT text FROM Choices
        WHERE screen_id = ?""", (self.current_id,)).fetchall()

    def write(self, text_screen, text_choices):
        pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = Game()
    ex.show()
    sys.exit(app.exec())