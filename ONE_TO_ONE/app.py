from  flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy import Column,Integer,String,ForeignKey

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///eample.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)

class parent(db.Model):
   id=db.Column(db.Integer,primary_key=True)
   name=db.Column(db.String(200),nullable=False)
   child=db.relationship('child',backref='parent',uselist=False)


class child(db.Model):
   id=db.Column(db.Integer,primary_key=True)  
   name=db.Column(db.String(200),nullable=False)  
   parent_id=db.Column(db.Integer,db.ForeignKey('parent.id'))