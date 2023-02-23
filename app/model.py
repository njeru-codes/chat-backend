from .database import Base
from sqlalchemy import Column, Integer,String, Float
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.types import Date, Time
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY



# Declare your database tables/models  here
class User(Base):
    __tablename__ ='user'
    id = Column(Integer, primary_key=True, nullable=False)
    email=Column(String, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text( 'NOW()') )

class Chat(Base):
    __tablename__ ='chat'
    id = Column(Integer, primary_key=True, nullable=False)
    users = Column(ARRAY(String) )
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text( 'NOW()') )

class Message(Base):
    __tablename__ ='message'
    id = Column(Integer, primary_key=True, nullable=False)
    sender = Column(String, nullable=False)
    receiver = Column(String, nullable=False)
    message = Column(String, nullable=False)
    chat_id = Column(Integer, primary_key=True, nullable=False)








