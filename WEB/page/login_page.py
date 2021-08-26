#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/06 14:08
# @Author  : zc
# @File    : login_page.py

from time import sleep
from WEB.locator.loginPage_loc import LoginPageLoc as loc
from WEB.page.base_page import Base
from WEB.page.main_page import MainPage


class LoginPage(Base):
    """登录页"""

    def login_action(self,mobile):
        """登录操作"""
        self.el_sendKeys(loc.mobile_loc,mobile)
        self.el_click(loc.checkBox_loc)
        self.el_click(loc.nextButton_loc)
        # 停顿20秒手动输入短信验证码
        sleep(20)
        self.el_click(loc.enterButton_loc)

    def goto_mainPage(self,mobile):
        """跳转到主页"""
        self.login_action(mobile)
        return MainPage(self.driver)