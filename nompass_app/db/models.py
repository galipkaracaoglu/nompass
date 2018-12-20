from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime
"""
import psycopg2
conn = psycopg2.connect("dbname=db user=postgres host=db")
"""
class Place(Base):
    __tablename__ = 'Place'
    id = Column(Integer,primary_key=True)
    name = Column(String(256))
    