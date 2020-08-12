#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : navupd.py
@Time    : 2020/5/25 14:57
@Author  : Shek
@Version : 1.0
@Contact : vflanker@163.com
@License : (C)Copyright 2020-2021, Shek Innovation
@Desc    : 
"""

# here put the import lib

from jinja2 import FileSystemLoader, Environment
import pprint


class H5Navigation:
    verbose = False
    KEY_PAGE, KEY_NAV = 'page', 'navigation'
    KEY_PAGE_HEAD_T, KEY_PAGE_MAIN_T, KEY_PAGE_SUB_T = 'head_title', 'main_title', 'sub_title'
    KEY_CONTENT, KEY_FONT, KEY_HREF, KEY_ICON = 'content', 'font', 'href', 'icon'

    __template_path = 'template.html'
    __default_font = 'Microsoft YaHei UI Light'
    __default_icon = 'fa fa-edge'
    __default_nav_item = {KEY_HREF: '', KEY_CONTENT: '未设置', KEY_ICON: __default_icon}
    __default_nav_count = 7
    __data_template = {
        KEY_PAGE: {KEY_PAGE_HEAD_T: '', KEY_PAGE_MAIN_T: {KEY_CONTENT: '', KEY_FONT: __default_font},
                   KEY_PAGE_SUB_T: {KEY_CONTENT: '', KEY_FONT: __default_font}},
        KEY_NAV: []}
    for i in range(__default_nav_count):
        __data_template[KEY_NAV].append({KEY_HREF: '', KEY_CONTENT: '未设置', KEY_ICON: __default_icon})

    def __init__(self):
        self.__data = self.__data_template.copy()
        pass

    def set_verbose(self, verbose: bool = True):
        self.verbose = verbose
        print('verbose:{}'.format(self.verbose))

    def set_head_title(self, content: str):
        self.__data[self.KEY_PAGE][self.KEY_PAGE_HEAD_T] = content

    def set_main_title(self, content: str, font: str = None):
        if font is None:
            font = self.__default_font
        self.__data[self.KEY_PAGE][self.KEY_PAGE_MAIN_T][self.KEY_CONTENT] = content
        self.__data[self.KEY_PAGE][self.KEY_PAGE_MAIN_T][self.KEY_FONT] = font

    def set_sub_title(self, content: str, font: str = None):
        if font is None:
            font = self.__default_font
        self.__data[self.KEY_PAGE][self.KEY_PAGE_SUB_T][self.KEY_CONTENT] = content
        self.__data[self.KEY_PAGE][self.KEY_PAGE_SUB_T][self.KEY_FONT] = font

    def set_navigations(self, items: list):
        for i, v in enumerate(items):
            self.__data[self.KEY_NAV][i][self.KEY_CONTENT] = v[0]
            self.__data[self.KEY_NAV][i][self.KEY_HREF] = v[1] if len(v) >= 2 else ''
            self.__data[self.KEY_NAV][i][self.KEY_ICON] = v[2] if len(v) == 3 else self.__default_icon
            if self.verbose:
                print('[+] 设置项目%d:\t"%s"\t=> "%s"' % (i + 1, v[0], v[1] if len(v) >= 2 else ''))
        for i in range(len(items), 7):
            if self.verbose:
                print('[-] 未设置项目%d:\t"%s"\t=> "%s"' % (i + 1, '未设置', ''))

    def check_data(self):
        pprint.pprint(self.__data)

    def generate(self, export_path: str = 'index.html'):

        env = Environment(loader=FileSystemLoader('./'))
        template = env.get_template(self.__template_path)
        with open(export_path, 'w', encoding='utf-8') as fp:
            html_content = template.render(data=self.__data)
            fp.write(html_content)
        print('generated: "%s" ' % export_path)
        self.deployment_help()

    @staticmethod
    def deployment_help():
        print('deployment: Use scp/sftp/ftp to ' +
              'upload file "index.html", directories "css" and "webfonts" to web directory of your web server.')
