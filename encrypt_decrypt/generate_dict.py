#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

###############################################################################
#                              generate_dict.py                               #
###############################################################################

import string


def generate_dict(password_chars=string.lowercase, password_len=3, dict_file='dict.txt'):
    """生成密码字典

    :password_chars: 密码所使用的字符
    :password_len: 密码长度
    :dict_file: 字典文件
    :returns: None

    """

    passwdchar_len = len(password_chars)
    i = 0
    imax = passwdchar_len**password_len
    with open(dict_file, "w") as f:
        while i < imax:
            temp = i
            password = ''
            j = 0
            while j < password_len:
                ch = temp % passwdchar_len
                password = password+password_chars[ch]
                temp = temp//passwdchar_len
                j += 1
            f.write(password[::-1]+'\n')
            i += 1
        f.write('\n')


if __name__ == "__main__":
    generate_dict()
