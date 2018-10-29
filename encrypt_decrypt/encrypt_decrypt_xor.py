#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

def encrypt_decrypt_xor(strx, key):
    """使用key中的每个字符和strx中的每个字符相异或以加/解密
    :arg1: strx, 待加/解密字符串
    :arg2: key, 加/解密使用的密钥
    :returns: result, 加/解密的结果

    """

    strx_len = len(strx)
    key_len=len(key)
    result = ''
    i=0
    while i<strx_len:
        result += chr(ord(strx[i]) ^ ord(key[i%key_len]))
        i+=1
    return result

def main():
    print encrypt_decrypt_xor('PSRUTWVYX[Z]\_', '1')
    print encrypt_decrypt_xor('abcdefghijklmn', '1')

if __name__ == "__main__":
    main()
