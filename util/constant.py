#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from PyQt5.Qt import QSettings
__author__ = 'xiwei'

HOME = os.getcwd()
RESOURCE = os.path.join(HOME, 'resource')
ICON = os.path.join(RESOURCE, 'images', 'icon.png')
UI = os.path.join(RESOURCE, 'ui', 'main.ui')
UI_LOGIN = os.path.join(RESOURCE, 'ui', 'login.ui')
STYLE = os.path.join(RESOURCE, 'ui', 'style.css')

CLIENT_ID = QSettings().value('client_id')
