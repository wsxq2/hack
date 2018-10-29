#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#######################################################################
#                        force_cracking_md5.py                        #
#######################################################################
import md5
import string

def main():
    passwordchar=string.lowercase # 密码使用的字符集
    password_len=5 # 密码的长度
    passwordchar_len=len(passwordchar) # 密码使用的字符集的长度
    i=0
    md5_hexdigest='21232f297a57a5a743894a0e4a801fc3' # md5摘要
    i_max=passwordchar_len**password_len 
    
    while i <i_max:
        temp=i
        password=''
        j=0
        while j<password_len:
            ch=temp%passwordchar_len
            password+=passwordchar[ch]
            temp=temp//passwordchar_len
            j+=1
        password=password[::-1]
        m=md5.new(password)
        s2=m.hexdigest()
        if s2 == md5_hexdigest:
            print password
            break
        i+=1

if __name__ == "__main__":
    main()
