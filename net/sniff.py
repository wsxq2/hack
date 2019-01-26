#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scapy.all import *
from scapy.layers.l2 import getmacbyip
#from scapy.all import sniff, ARP


def prn(pkt):
    print pkt.summary()


def get_mac_by_ip(ip):
    pkt = ARP(pdst=ip)
    ans = sr(pkt)
    return ans[0][0][1].hwdst


def main():
    # sniff(filter='icmp', prn=prn)
    print getmacbyip('192.168.56.16')


if __name__ == "__main__":
    get_mac_by_ip('192.168.56.16')
