#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

###############################################################################
#                            force_cracking_md5.py                            #
###############################################################################

import md5
import string


def force_cracking_md5(md5_hexdigest, dict_file='./dict.txt'):
    """暴力破解 md5

    :md5_hexdigest: md5 摘要，即密文（ciphertxt）
    :returns: 明文（cleartxt）

    """
    with open(dict_file, "r") as f:
        for password in f:
            m = md5.new(password.strip('\n'))
            md5_hexdigest_test = m.hexdigest()
            if md5_hexdigest_test == md5_hexdigest:
                return password


if __name__ == "__main__":
    print force_cracking_md5(md5.new('admin').hexdigest())
