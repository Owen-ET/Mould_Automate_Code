#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/06 16:26
# @Author  : zc
# @File    : main_page.py

from time import sleep
from WEB.page.base_page import Base
from WEB.locator.mainPage_loc import MainPageloc as loc
from WEB.page.calendar_page import CalendarPage


class MainPage(Base):
    """飞书主页"""

    def main_action(self):
        """主页操作"""
        self.el_click(loc.left_calendar_loc)
        sleep(0.5)
        self.enter_window(2)

    def goto_calendarPage(self):
        """跳转到日历页面"""
        self.main_action()
        return CalendarPage(self.driver)