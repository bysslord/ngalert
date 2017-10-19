#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import util.constant
from PyQt5.Qt import QApplication, QSystemTrayIcon, QIcon, QMenu
from util.logger import log


class Menu(QMenu):
    def __init__(self, parent, *__args):
        super().__init__(*__args)
        self.parent = parent   # type: Tray

        self.addAction('test', self.parent.test)
        self.addAction('退出', self.parent.exit)


class Tray(QSystemTrayIcon):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setIcon(QIcon(util.constant.ICON))
        self.setContextMenu(Menu(self))
        self.test()

    def test(self):
        log.info('test{}'.format(self.supportsMessages()))
        self.showMessage('test', 'test')

    @staticmethod
    def exit():
        app.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName('ngalert')
    tray = Tray(app)
    tray.show()
    tray.showMessage('test', 'test')
    sys.exit(app.exec())
