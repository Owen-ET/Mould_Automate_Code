#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/05 09:11
# @Author  : zc
# @File    : base.py
import requests

from API.utils.functions import Functions


class Base:

    def __init__(self):

        self.s = requests.Session()
        self.token = self.get_token()
        self.s.headers = {
            'Authorization': f"Bearer {self.token}",
            'Content-Type': "application/json; charset=utf-8"
        }

        self.baseUrl = self.base['calendarsUrl']
        self.list = []

    def get_token(self):
        '''获取token'''
        self.base = Functions().getYamlData('base')
        url = self.base['token']['url']
        params = self.base['token']['params']
        r = self.send('POST',url,json=params).json()
        return r['tenant_access_token']

    def send(self,*args,**kwargs):
        return self.s.request(*args,**kwargs)