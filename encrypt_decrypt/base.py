#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

###############################################################################
#                                   base.py                                   #
###############################################################################


import base64
import string
import random


encrypt_times = 10


def get_base(ciphertext):
    """get the base according string ciphertext

    :ciphertext: string, such as 'ABCDEF1234567890'
    :returns: base, such as '16'

    """
    # 10+6
    b16 = string.digits + 'ABCDEF'
    # 26+6+1
    b32 = string.ascii_uppercase + '234567='
    # 10+26*2+2+1
    b64 = string.digits + string.letters + '+/='

    bdict = {'64': b64, '32': b32, '16': b16}
    all_char = set(ciphertext)

    for key in sorted(bdict.keys()):
        if all_char.issubset(bdict[key]):
            return key


def decrypt(ciphertext):
    """decrypt the `ciphertext` `encrypt_times` times with base64.bxxdecode package.

    :ciphertext: ciphertext
    :returns: cleartext

    """
    base_decode = {'16': base64.b16decode,
                   '32': base64.b32decode, '64': base64.b64decode}
    cleartext = ciphertext+''
    for i in range(encrypt_times):
        cleartext = base_decode[get_base(cleartext)](cleartext)
    return cleartext


def encrypt(cleartext):
    """encrypt the `cleartext` `encrypt_times` times with base64.bxxencode package.

    :cleartext: cleartext
    :returns: ciphertext

    """
    base_encode = {'16': base64.b16encode,
                   '32': base64.b32encode, '64': base64.b64encode}
    ciphertext = cleartext+''

    for i in range(encrypt_times):
        base = random.choice(['16', '32', '64'])
        ciphertext = base_encode[base](ciphertext)

    return ciphertext


if __name__ == "__main__":
    ciphertext = encrypt('flag{ some secret }')
    print 'ciphertext:\n', ciphertext
    print '\ncleartext:\n', decrypt(ciphertext)
