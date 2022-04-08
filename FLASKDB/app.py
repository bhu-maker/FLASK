from collections import UserList
from email.mime import base
from unicodedata import name
from click import echo
from sqlalchemy import Column,Integer,String,ForeignKey,create_engine
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker
import os

BASE_DIR=os.path.dirname(os.path.realpath(__file__))

conn_str='sqlite:///'+os.path.join(BASE_DIR,'data.db')
engine=create_engine(conn_str,echo=True)
Base=declarative_base()


#app=Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost:3306/relation'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#db=SQLAlchemy(app)

class parent(Base):
    __tablename__='parents'
    id=Column(Integer(),primary_key=True)
    name=Column(String(45),nullable=False)
    child=relationship('child',back_populates='parent',uselist=False,cascade="all,delete")

    def __repr__(self):
        return f"<parent {self.id}>"    

   
class child(Base):
    __tablename__='children'
    id=Column(Integer(),primary_key=True)
    name=Column(String(45),nullable=False)
    parent_id=Column(Integer(),ForeignKey('parents.id',ondelete="CASCADE"))
    parent=relationship('parent',back_populates='child')

    def __repr__(self):
        return f"<child {self.id}>"
    
Base.metadata.create_all(engine)
session=sessionmaker()(bind=engine)

