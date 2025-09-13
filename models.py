from sqlalchemy import Column, Integer, String, Boolean
from db import Base

class Feedback(Base):
     __tablename__ = "feedback"

     id = Column(Integer, primary_key=True, index=True)
     name = Column(String)
     comment = Column(String)

class User(Base):
     __tablename__ = "users"

     id = Column(Integer, primary_key=True, index=True)
     name = Column(String)
     email = Column(String, unique=True, index=True)

class Product(Base):
     __tablename__ = "products"
     
     product_id = Column(Integer, primary_key = True, index=True)
     product_name = Column(String)
     quantity = Column(Integer)
     in_stock = Column (Boolean)