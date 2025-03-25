from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class PacketLog(Base):
    __tablename__ = 'packets'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    src_ip = Column(String(15))
    dst_ip = Column(String(15))
    protocol = Column(String(10))
    length = Column(Integer)
    payload = Column(String(500))

class AlertLog(Base):
    __tablename__ = 'alerts'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    alert_type = Column(String(50))
    source_ip = Column(String(15))
    details = Column(String(200))

class DBLogger:
    def __init__(self, db_path='sqlite:///logs/packets.db'):
        self.engine = create_engine(db_path)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        
    def log_packet(self, packet_data):
        session = self.Session()
        packet = PacketLog(
            timestamp=datetime.now(),
            src_ip=packet_data['src_ip'],
            dst_ip=packet_data['dst_ip'],
            protocol=packet_data['protocol'],
            length=packet_data['length'],
            payload=str(packet_data['payload'])[:500]
        )
        session.add(packet)
        session.commit()
        session.close()

    def log_alert(self, alert_type, source_ip, details):
        session = self.Session()
        alert = AlertLog(
            timestamp=datetime.now(),
            alert_type=alert_type,
            source_ip=source_ip,
            details=details
        )
        session.add(alert)
        session.commit()
        session.close()