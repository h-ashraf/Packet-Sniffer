from colorama import Fore, Style
from .sniffer import PacketSniffer
from .logger import DBLogger
import argparse
import time

def display_banner():
    print(f"""{Fore.CYAN}
    ██████╗  █████╗  ██████╗██╗  ██╗███████╗████████╗
    ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝╚══██╔══╝
    ██████╔╝███████║██║     █████╔╝ █████╗     ██║   
    ██╔═══╝ ██╔══██║██║     ██╔═██╗ ██╔══╝     ██║   
    ██║     ██║  ██║╚██████╗██║  ██╗███████╗   ██║   
    ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝   
    {Style.RESET_ALL}""")

def main():
    parser = argparse.ArgumentParser(description='Network Packet Sniffer with IDS')
    parser.add_argument('-i', '--interface', default='eth0', help='Network interface')
    parser.add_argument('-f', '--filter', default='tcp or udp', help='BPF filter')
    args = parser.parse_args()

    display_banner()
    print(f"{Fore.YELLOW}[*] Starting sniffer on interface {args.interface}{Style.RESET_ALL}")
    
    sniffer = PacketSniffer()
    try:
        sniffer.start(interface=args.interface, filter=args.filter)
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Stopping sniffer...{Style.RESET_ALL}")

if __name__ == '__main__':
    main()