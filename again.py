import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from datetime import datetime


class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('welcome1.ui', self)
        self.current_id = 1
        self.pushWelcome.clicked.connect(self.get_result)
        self.text_screen = ''
        self.text_slide = []
        self.text_button = []
        self.next_slides_id = []
        self.slide = None
        self.con = sqlite3.connect('project.sqlite')
        self.clickable = True
        self.additional_text = ''
        # self.start_time = datetime.now.time()
        # self.end_time = 0

    def get_result(self):
        '''"Вытаскивает" нужный текст из таблицы'''
        cur = self.con.cursor()
        self.text_screen = self.additional_text + cur.execute("""SELECT text FROM Screens
        WHERE id = ?""", (self.current_id,)).fetchone()[0]
        self.slide_text.setText(self.text_screen)
        self.text_slide = cur.execute("""SELECT text FROM Choices
        WHERE screen_id = ?""", (self.current_id,)).fetchone()[0]
        self.text_button = cur.execute("""SELECT text, next_screen, additional_text FROM Buttons
        WHERE choice_id = ?""", (self.current_id,)).fetchall()
        self.text_button, self.next_slides_id, self.additional_texts = (list(map(lambda x: x[0], self.text_button)),
                                                                        list(map(lambda x: x[1], self.text_button)),
                                                                        list(map(lambda x: x[2], self.text_button)))
        self.pushWelcome.setText('Продолжить')
        self.pushWelcome.clicked.connect(self.write)

    def write(self):
        '''Записывает текст в диалоговое окно'''
        if self.clickable:
            self.slide = Slide(text_slide=self.text_slide,
                               text_button=self.text_button,
                               next_slides_id=self.next_slides_id,
                               game=self,
                               additional_texts=self.additional_texts)
            self.slide.show()
            self.clickable = False

        '''cur = self.con.cursor()
        text, ok_pressed = QInputDialog().getInt(self, "Введите имя", *self.text_choices)
        if ok_pressed:
            self.textBrowser.setText(self.text_screen)'''

    def insert_statistics(self):
        '''Добавляет номер игрока, время и концовку в таблицу'''
        # self.time_ = datetime.now().time - self.start_time
        statistics_insert_statistics = '''INSERT INTO Statistics (time,end) VALUES(self.time_, self.end_)'''
        # time_ - время / end_ - номер концовки


class Slide(QDialog):
    def __init__(self, text_slide, text_button, next_slides_id, game, additional_texts):
        super().__init__()
        uic.loadUi('dialog.ui', self)
        self.text_slide = text_slide
        self.text_button = text_button
        self.next_slides_id = next_slides_id
        self.game = game
        self.additional_texts = additional_texts
        self.label.setText(self.text_slide)
        self.push_button_1.setText(self.text_button[0])
        self.push_button_2.setText(self.text_button[1])

        # self.pixmap = QPixmap(image)
        # self.label.setPixmap(self.pixmap)

        for num, button in enumerate([self.push_button_1, self.push_button_2]):
            button.clicked.connect(self.make_choice(num))

    def make_choice(self, num):
        def press_info():
            self.hide()
            self.game.current_id = self.next_slides_id[num]
            self.game.clickable = True
            if self.additional_texts[num]:
                self.game.additional_text = self.additional_texts[num] + '\n'
            else:
                self.game.additional_text = ''

        return press_info

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
