#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

###############################################################################
#                                   xor.py                                    #
###############################################################################


def encrypt_decrypt_xor(strx, key):
    """使用 key 中的每个字符和 strx 中的每个字符相异或以加/解密

    :arg1: strx, 待加/解密字符串
    :arg2: key, 加/解密使用的密钥
    :returns: result, 加/解密的结果

    """

    strx_len = len(strx)
    key_len = len(key)
    result = ''
    i = 0
    while i < strx_len:
        result += chr(ord(strx[i]) ^ ord(key[i % key_len]))
        i += 1
    return result


if __name__ == "__main__":
    print encrypt_decrypt_xor('abcdefghijklmn', '54321')
    print encrypt_decrypt_xor('TVPVTSS[[[^X^\\', '54321')
