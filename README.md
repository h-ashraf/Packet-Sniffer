# PacketSniffer-X 🔍🛡️

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Open Issues](https://img.shields.io/github/issues-raw/h-ashraf/PacketSniffer)](https://github.com/yourusername/PacketSniffer-X/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

A professional network packet analysis tool with real-time intrusion detection capabilities.

## Table of Contents
- [Features](#features-)
- [Installation](#installation-)
- [Usage](#usage-)
- [Configuration](#configuration-)
- [Detection Rules](#detection-rules-)
- [Ethical Considerations](#ethical-considerations-)
- [Contributing](#contributing-)
- [License](#license-)
- [Acknowledgements](#acknowledgements-)

## Features ✨

### Core Functionality
- Real-time packet capture (TCP/UDP/ICMP/HTTP)
- Protocol-specific analysis
- BPF filter support
- Multi-interface monitoring

### Security Features
- SYN Flood detection
- Port Scanning detection
- Unauthorized access alerts
- Custom rule engine

### Output & Logging
- SQLite database storage
- JSON export capability
- Color-coded CLI interface
- Alert notification system

## Installation ⚙️

### Prerequisites
- Python 3.8+
- Root/Admin privileges
- libpcap-dev (Linux) / WinPcap (Windows)


# Clone repository
```bash 
git clone https://github.com/yourusername/PacketSniffer-X.git
cd PacketSniffer-X
```
# Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate  # Windows
```

# Install dependencies
```bash
pip install -r requirements.txt
```

# Usage 🚀

## Basic Monitoring
```bash
sudo python src/cli.py -i eth0
```

## Advanced Filtering

```bash
# Monitor HTTP traffic only
sudo python src/cli.py -i eth0 -f "tcp port 80"

# Track specific IP range
sudo python src/cli.py -i eth0 -f "net 192.168.1.0/24"
```

## Command Line Options

```bash
  -h, --help            show help message
  -i INTERFACE, --interface INTERFACE
                        Network interface (default: eth0)
  -f FILTER, --filter FILTER
                        BPF filter (default: tcp or udp)
  -v, --verbose         Enable verbose output
  ```

# Configuration ⚙️

## Database Settings

Create .env file:

```bash
DB_PATH=logs/packets.db
LOG_LIMIT=5000  # Max stored packets
ALERT_TTL=3600  # Alert retention in seconds
```

## Detection Thresholds

Modify src/detector.py:

```bash
# SYN Flood detection
SYN_FLOOD_THRESHOLD = 100  # Packets per 5 seconds

# Port Scan detection
PORT_SCAN_THRESHOLD = 5  # Attempts per port
SCAN_WINDOW = 60         # Detection window in seconds
```
# Ethical Considerations ⚖️

## Legal Compliance

Use only on networks you own or have explicit written authorization to monitor
Comply with local privacy laws (GDPR, CCPA, etc.)
Never capture sensitive personal data

## Responsible Usage
1. Always inform network users about monitoring activities
2. Avoid capturing payload content when possible
3. Regularly purge captured data
4. Use encryption for stored logs

# Contributing 🤝

## Development Setup
```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# Build documentation
mkdocs build
```
## Contribution Process

1) Fork the repository

2) Create feature branch (```git checkout -b feature/your-feature```)

3) Commit changes (``` git commit -m 'Add amazing feature'```)

4) Push to branch (```git push origin feature/your-feature```)

5) Open Pull Request
