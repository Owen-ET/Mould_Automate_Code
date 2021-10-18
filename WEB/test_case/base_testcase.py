#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/26 10:06
# @Author  : zc
# @File    : base_testcase.py

from WEB.page.web import Web
from WEB.utils.functions import Functions as Fun


class BaseTestCase:
    loginData = Fun().getYamlData("login")

    def setup(self):
        """开启测试用例"""
        self.web = Web().startWeb(self.loginData['url'])
        self.login = self.web.goto_loginPage()

    def teardown(self):
        """关闭测试用例"""
        # Web().stopWeb()
        self.web.stopWeb()