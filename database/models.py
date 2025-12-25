"""
Database models - SQLAlchemy
"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from pathlib import Path

# Base
Base = declarative_base()

# Engine
db_path = Path(__file__).parent / 'twitter.db'
engine = create_engine(f'sqlite:///{db_path}')

# Session
Session = sessionmaker(bind=engine)


class Conta(Base):
    """Modelo de conta Twitter"""
    __tablename__ = 'contas'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(100))
    email = Column(String(200))
    api_key = Column(String(200))
    status = Column(String(50), default='ativa')
    criado_em = Column(DateTime, default=datetime.now)


def get_session():
    """Retorna sessão do banco"""
    Base.metadata.create_all(engine)
    return Session()