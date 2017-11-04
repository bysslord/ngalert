#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xiwei'

import requests
from util.logger import log


class NgAlertD(object):
    _host = 'http://localhost:9757'

    def __init__(self, username, password, client_id=None):
        self.username = username
        self.password = password
        self.client_id = client_id

    def _request(self, url, params, data=None):
        _url = f'{self._host}/{url}'
        try:
            if data:
                res = requests.post(_url, params, data)
            else:
                res = requests.get(_url, params)
        except Exception as e:
            log.error(f'Connect to {_url} failed, cause by: {e}')

    def client_login(self):
        return self._request(
            'client/login',
            {
                "username": self.username,
                "password": self.password,
                "client_id": self.client_id
            }
        )
