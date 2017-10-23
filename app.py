#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QCloseEvent

import util.constant
from PyQt5.Qt import QApplication, QSystemTrayIcon, QIcon, QMenu
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit
from PyQt5.uic import loadUi
from util.logger import log


class MainWindow(QWidget):
    def __init__(self, parent, *__args):
        super().__init__(*__args)
        self.tray = parent
        loadUi(util.constant.UI, self)

    def closeEvent(self, event: QCloseEvent):
        event.ignore()
        self.hide()


class LoginWindow(QWidget):
    pushButton_login: QPushButton
    lineEdit_username: QLineEdit
    lineEdit_password: QLineEdit

    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tray = parent
        loadUi(util.constant.UI_LOGIN, self)

    def login(self):
        username, password = self.lineEdit_username.text(), self.lineEdit_password.text()
        if not (username and password):
            self.tray.showMessage('提示', '请输入用户名密码')
            return
        print(username, password)


class Menu(QMenu):
    def __init__(self, parent, *__args):
        super().__init__(*__args)
        self.parent = parent  # type: Tray

        self.addAction('主界面', self.parent.show_main_window)
        self.addAction('退出', self.parent.exit)


class Tray(QSystemTrayIcon):
    window: MainWindow

    def __init__(self, *__args):
        super().__init__(*__args)
        self.window = None
        self.setIcon(QIcon(util.constant.ICON))
        self.setContextMenu(Menu(self))
        self.setting = QSettings()
        self.show_main_window()

    @property
    def is_login(self):
        return self.setting.value('token', defaultValue=None)

    def _create_window(self):
        if self.window:
            del self.window
        if self.is_login:
            log.info('Token {} found, show main window'.format(type(self.is_login)))
            return MainWindow(self)
        else:
            log.info('No token found, show login')
            return LoginWindow(self)

    def show_main_window(self):
        if not self.window:
            self.window = self._create_window()
        self.window.show()

    @staticmethod
    def exit():
        app.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setOrganizationName('IONull')
    app.setOrganizationDomain('ionull.com')
    app.setApplicationName('ngalert')
    app.setWindowIcon(QIcon(util.constant.ICON))
    with open(util.constant.STYLE, 'r') as style:
        app.setStyleSheet(style.read())
    tray = Tray(app)
    tray.show()
    sys.exit(app.exec())
