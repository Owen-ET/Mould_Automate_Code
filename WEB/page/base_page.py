#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/06 11:30
# @Author  : zc
# @File    : base_page.py

from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC


class Base:

    def __init__(self,driver: WebDriver):
        self.driver = driver

    def find_element(self,loc):
        """查找元素"""
        return self.driver.find_element(*loc)

    def find_elements(self,loc):
        """查找多组元素"""
        return self.driver.find_element(*loc)

    def el_click(self,loc):
        """点击事件"""
        self.webDriverWait(loc).click()

    def el_sendKeys(self,loc,text):
        """输入事件"""
        self.webDriverWait(loc).send_keys(text)

    def webDriverWait(self,loc):
        """显式等待，查找元素"""
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
        return self.find_element(loc)

    def handles(self):
        """获取所有页面handles"""
        return self.driver.window_handles

    def enter_window(self,index):
        """进入页面"""
        handles = self.handles()
        self.driver.switch_to.window(handles[index-1])

    def get_text(self,loc):
        """获取文字内容"""
        return self.webDriverWait(loc).text

    def move_to_element(self,loc):
        """移动鼠标到元素上"""
        AC(self.driver).move_to_element(self.webDriverWait(loc)).perform()

    def el_clear(self,loc):
        """清空数据"""
        self.webDriverWait(loc).clear()

    def el_clear_sendKeys(self,loc,text):
        """清空数据并输入数据"""
        self.webDriverWait(loc).clear()
        self.el_sendKeys(loc,text)