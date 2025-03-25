from scapy.all import sniff, Ether, IP, TCP, UDP
from scapy.layers.http import HTTP
from .logger import DBLogger
from .detector import IntrusionDetector
import time

class PacketSniffer:
    def __init__(self):
        self.logger = DBLogger()
        self.detector = IntrusionDetector(self.logger)
        
    def _process_packet(self, packet):
        packet_data = {
            'src_ip': None,
            'dst_ip': None,
            'protocol': None,
            'src_port': None,
            'dst_port': None,
            'length': len(packet),
            'payload': None,
            'flags': None
        }

        if IP in packet:
            packet_data['src_ip'] = packet[IP].src
            packet_data['dst_ip'] = packet[IP].dst
            packet_data['protocol'] = packet[IP].proto

        if TCP in packet:
            packet_data['src_port'] = packet[TCP].sport
            packet_data['dst_port'] = packet[TCP].dport
            packet_data['flags'] = packet[TCP].flags
            packet_data['payload'] = bytes(packet[TCP].payload)
        elif UDP in packet:
            packet_data['src_port'] = packet[UDP].sport
            packet_data['dst_port'] = packet[UDP].dport

        # Log to database
        self.logger.log_packet(packet_data)
        
        # Run intrusion detection
        self.detector.detect_syn_flood(packet_data)
        self.detector.detect_port_scan(packet_data)

    def start(self, interface='eth0', filter='tcp or udp'):
        sniff(prn=self._process_packet, store=0, iface=interface, filter=filter)