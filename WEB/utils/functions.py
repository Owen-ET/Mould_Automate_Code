#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/06 13:46
# @Author  : zc
# @File    : functions.py

import os
import yaml


class Functions:

    def curPath(self):
        """获取本层目录"""
        basePath = os.path.dirname(os.path.abspath(__file__))
        return basePath

    def upPath(self):
        """获取上级目录路径"""
        basePath = os.path.dirname(os.path.dirname(__file__))
        return basePath

    def getYamlData(self,yamlName):
        """获取yaml数据"""
        yamlPath = self.upPath() + f'/data/{yamlName}Data.yaml'
        with open(yamlPath,encoding='utf-8') as file:
            data = yaml.load(file,Loader=yaml.FullLoader)
        return data[yamlName]