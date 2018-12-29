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
    adress = Column(String(10000))
    cordinate_lat = Column(String(50))
    cordinate_lot = Column(String(50))
    general_point = Column(Integer,default=1)
    city = Column(String(70))
    semt = Column(String(70))

    