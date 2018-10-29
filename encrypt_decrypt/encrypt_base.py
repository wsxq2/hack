#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#######################################################################
#                           encrypt_base.py                           #
#######################################################################

import base64
import random
def main():
    """program entrance
    """
    cleartext='flag{some txt}'
    base_encode={'16': base64.b16encode, '32': base64.b32encode, '64': base64.b64encode}
    ciphertext=cleartext+''
    for i in range(10):
        base=random.choice(['16', '32', '64'])
        ciphertext=base_encode[base](ciphertext)

    with open('a.txt','wb') as f:
        f.write(ciphertext)
        

if __name__ == "__main__":
    main()



