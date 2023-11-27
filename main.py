import sys

import pygame

from design import Ui_Dialog, Ui_Mainwin, OpenFileDialog, Dialog_urlfile
from design import Genre_dialog
from PyQt5.QtWidgets import QApplication, QFileDialog, QTableWidgetItem
from PyQt5 import QtGui
from PyQt5.Qt import *

import sqlite3
import hashlib
import datetime

db = sqlite3.connect('C:\\Users\\66964\\Desktop\\coding like wxtchblade\\Проекты Python\\music_player\\musplayer.db')
cur = db.cursor()

user = ''
choose, genre = '', ''


class LoginForm(Ui_Dialog):
    def __init__(self):
        super().__init__()

        self.flag = False

        self.loginButton.clicked.connect(self.log_app)
        self.createaccButton.clicked.connect(self.reg_app)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        if self.flag:
            a0.accept()
        else:
            a0.ignore()

    def log_app(self):
        if self.login and self.password:
            try:
                passw = hashlib.md5(self.password.text().encode()).hexdigest()
                cur.execute(
                    f'SELECT login, password FROM users WHERE login = ? AND password = ?', (self.login.text(), passw))
            except Exception:
                pass

            if not cur.fetchone():
                self.incorrectLabel.setText('Неверный логин/пароль')
            else:
                global user
                user = self.login.text()
                self.flag = True
                self.close()
        else:
            self.incorrectLabel.setText('Введите логин/пароль')

    def reg_app(self):
        if self.login and self.password:
            passw = hashlib.md5(self.password.text().encode()).hexdigest()
            cur.execute('INSERT INTO users (login, password) VALUES (?, ?)', (self.login.text(), passw))
            db.commit()
        else:
            self.incorrectLabel.setText('Введите логин/пароль')


class Choose_genre(Genre_dialog):
    def __init__(self):
        super().__init__()

        self.pushButton.clicked.connect(self.accept_genre)

    def accept_genre(self):
        global genre

        if self.lineEdit.text():
            genre = self.lineEdit.text()
            self.close()


class MainWin(Ui_Mainwin):
    def __init__(self):
        super().__init__()
        LoginForm().exec()
        self.flag, self.counter = False, False
        self.con_lsts = []
        self.mix = pygame.mixer
        self.mix.init()
        self.print_hello()
        self.ID = ''
        self.loadButton.clicked.connect(self.open_music)
        self.tableWidget.cellClicked.connect(self.cell_was_clicked)
        self.playButton.clicked.connect(self.play_music)
        self.pauseButton.clicked.connect(self.pause_music)
        self.volumeChange.setValue(60)
        self.mix.music.set_volume(0.6)
        self.volumeChange.valueChanged[int].connect(self.change_volume)
        self.prevButton.clicked.connect(self.prev_music)
        self.nextButton.clicked.connect(self.next_music)
        self.refresh_table()
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setSortIndicator(0, Qt.AscendingOrder)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().sectionClicked.connect(self.sort_table)
        self.ordtype = Qt.DescendingOrder

    def refresh_table(self):
        names = []
        genres = []
        length = []
        ch = cur.execute('SELECT music_id FROM users WHERE login = ?', (user,)).fetchone()
        if ch[0] is None or ch == '':
            return
        music_ids = self.get_ids_from_users()
        for i in music_ids:
            music_name = cur.execute("""SELECT name FROM music
            INNER JOIN users ON music.id = ? AND users.login = ?""", (i, user)).fetchone()
            music_genre = cur.execute("""SELECT genre FROM music
            INNER JOIN users ON music.id = ? AND users.login = ?""", (i, user)).fetchone()
            music_length = cur.execute("""SELECT length FROM music
            INNER JOIN users ON music.id = ? AND users.login = ?""", (i, user)).fetchone()
            names.append(music_name[0])
            genres.append(music_genre[0])
            length.append(music_length[0])
        self.con_lsts = self.concatlsts(names, genres, length)

        self.tableWidget.setColumnCount(len(self.con_lsts[0]))
        self.tableWidget.setRowCount(len(self.con_lsts))
        self.tableWidget.setHorizontalHeaderLabels(['Название', 'Жанр', 'Продолжительность'])

        for row in range(len(names)):
            for column in range(len(self.con_lsts[0])):
                self.tableWidget.setItem(row, column, QTableWidgetItem(self.con_lsts[row][column]))

    def sort_table(self, index):
        if self.ordtype == Qt.DescendingOrder:
            self.ordtype = Qt.AscendingOrder
        else:
            self.ordtype = Qt.DescendingOrder
        self.tableWidget.sortItems(index, self.ordtype)

    def concatlsts(self, lst1: list, lst2: list, lst3: list):
        t = []
        for i in range(len(lst1)):
            t.append([lst1[i], lst2[i], lst3[i]])
        return t

    def cell_was_clicked(self, row, column):
        item = self.tableWidget.item(row, column)
        self.ID = item.text()

    def print_hello(self):
        global user
        t = datetime.datetime.now().hour
        if 12 > t >= 7:
            self.helloLabel.setText(f'Доброе утро, {user}')
        elif 18 > t >= 12:
            self.helloLabel.setText(f'Добрый день, {user}')
        elif 22 > t >= 18:
            self.helloLabel.setText(f'Добрый вечер, {user}')
        else:
            self.helloLabel.setText(f'Доброй ночи, {user}')

    def transform_path_to_name(self, lst: list):
        lst, lst_names = [i.split('/') for i in [lst]], []

        for i in lst:
            for k in i:
                if k == i[-1]:
                    lst_names.append(k.replace('.mp3', ''))
        return lst_names

    def lst_add_ind(self, lst: list, id: int):
        f = True
        for i in lst:
            if id in i:
                f = False
                break
        if f:
            lst.append(tuple(id))

    def transfrom_lstTuple_to_str(self, lst: list):
        t = ''
        for i in lst:
            t += ' '.join(i)
        return t

    def transform_lstTuple_to_lst(self, lst: list):
        t = []
        a = ''
        for i in lst:
            for k in i:
                t.append(k)
        return t

    def get_ids_from_users(self):
        global user

        req = cur.execute('SELECT music_id FROM users WHERE login = ?', (user,)).fetchone()
        res = self.transfrom_lstTuple_to_str([req]).split(', ')
        return res

    def refactor_minutes_seconds(self, ln):
        if ln < 60:
            return ln
        else:
            min = ln // 60
            sec = ln % 60
            return f'{int(min)}мин, {int(sec)}сек'

    def open_music(self):
        self.flag = True
        name_f = QFileDialog.getOpenFileName(
            self, 'Выбрать музыку', '', 'Музыка (*.mp3)')[0]

        name = self.transform_path_to_name(name_f)

        name = ''.join(name)

        req_n = cur.execute('SELECT name FROM music WHERE name = ?', (name,)).fetchone()
        req_g = cur.execute('SELECT genre FROM music WHERE name = ?', (name,)).fetchone()

        global genre
        global user

        if req_n is None:
            gen = Choose_genre()
            gen.exec()
        if req_n is not None:
            genre = req_g[0]
        if genre:
            ln = self.mix.Sound(name_f).get_length()
            ln_con = self.refactor_minutes_seconds(ln)
            ins_music = 'INSERT INTO music (name, genre, length) VALUES (?, ?, ?)'
            try:
                cur.execute(ins_music, (name, genre, ln_con))
                db.commit()
            except sqlite3.IntegrityError:
                pass
            cur.execute('UPDATE music SET path = ? WHERE name = ?', (name_f, name))
            db.commit()

            id_music = cur.execute('SELECT id FROM music WHERE name = ?', (name,)).fetchone()

            check = cur.execute('SELECT music_id FROM users WHERE login = ?', (user,)).fetchall()
            if check[0][0] is not None:
                t = self.transfrom_lstTuple_to_str(check).split(', ')

                if str(id_music[0]) not in t:
                    cur.execute('UPDATE users SET music_id = music_id || ", " || ? WHERE login = ?',
                                (str(id_music[0]), user))
            else:
                cur.execute('UPDATE users SET music_id = ? WHERE login = ?', (str(id_music[0]), user))
            db.commit()
            self.refresh_table()

    def play_music(self):
        if self.ID:
            if self.counter:
                self.mix.music.unpause()
                self.counter = False
                return
            path = cur.execute('SELECT path FROM music WHERE name = ?', (self.ID,)).fetchone()
            name = cur.execute('SELECT name FROM music WHERE name = ?', (self.ID,)).fetchone()
            self.mix.music.load(path[0])
            self.nameLabel.setText(name[0])
            self.mix.music.play()
        else:
            self.nameLabel.setText('выберите музыку перед прослушиванием')

    def pause_music(self):
        self.mix.music.pause()
        self.counter = True

    def change_volume(self):
        vol = self.volumeChange.value() / 100
        self.mix.music.set_volume(vol)

    def prev_music(self):
        ind = 0
        for i in self.con_lsts:
            if i[0] == self.ID:
                if self.con_lsts.index(i) == 0:
                    self.play_music()
                    return
                ind = self.con_lsts.index(i) - 1
                self.ID = self.con_lsts[ind][0]
                break
        self.play_music()

    def next_music(self):
        ind = 0
        for i in self.con_lsts:
            if i[0] == self.ID:
                if self.con_lsts.index(i) == len(self.con_lsts) - 1:
                    self.play_music()
                    return
                ind = self.con_lsts.index(i) + 1
                self.ID = self.con_lsts[ind][0]
                break
        self.play_music()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec())
