from collections import defaultdict
from datetime import datetime, timedelta

class IntrusionDetector:
    def __init__(self, logger):
        self.logger = logger
        self.syn_counter = defaultdict(int)
        self.port_scan_counter = defaultdict(int)
        self.window_start = datetime.now()
        
    def detect_syn_flood(self, packet):
        if packet['protocol'] == 'TCP' and packet['flags'] == 'S':
            self.syn_counter[packet['src_ip']] += 1
            
            # Reset counter every 5 seconds
            if datetime.now() - self.window_start > timedelta(seconds=5):
                self.syn_counter.clear()
                self.window_start = datetime.now()
                
            if self.syn_counter[packet['src_ip']] > 100:  # Threshold
                self.logger.log_alert(
                    'SYN Flood Attack',
                    packet['src_ip'],
                    f"Excessive SYN packets ({self.syn_counter[packet['src_ip']]})"
                )

    def detect_port_scan(self, packet):
        if packet['protocol'] == 'TCP' and packet['flags'] == 'S':
            key = f"{packet['src_ip']}-{packet['dst_port']}"
            self.port_scan_counter[key] += 1
            
            if self.port_scan_counter[key] > 5:  # Threshold
                self.logger.log_alert(
                    'Port Scanning',
                    packet['src_ip'],
                    f"Multiple connection attempts to port {packet['dst_port']}"
                )