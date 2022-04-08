

from dataclasses import fields
from pyexpat import model
from flask import Flask, jsonify,redirect,render_template,request,session
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost:3306/relation'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)
app.secret_key="relation"
marsh=Marshmallow(app)
CORS(app)

class profiles(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    person=db.Column(db.String(225),nullable=False)
    experience=db.Column(db.Integer,nullable=False)
    role=db.Column(db.String(200),nullable=False)
    ctc=db.Column(db.Float,nullable=False)
    expected=db.Column(db.Float,nullable=False)

    def __init__(self,p="",e=0,r="",c=0.0,ex=0.0) :
        self.person=p
        self.experience=e
        self.role=r
        self.ctc=c
        self.expected=ex

    def __repr__(self)->str:
        return f"{self.person} - {self.role}"

class profileschema(marsh.Schema):
    class Meta:
        fields=('id','person','role','experience','ctc','expected')

single_schema=profileschema()
many_schema=profileschema(many=True)

@app.route("/rest/",methods=['GET'])
def toall():
     obj=profiles.query.all()
     decrypt=many_schema.dump(obj)
     return jsonify(decrypt)


@app.route("/rest/<int:key>",methods=['GET'])
def individual(key):
    obj=profiles.query.filter_by(id=key).first()
    return single_schema.jsonify(obj)

@app.route("/rest/post",methods=['POST'])    
def posting():
       obj=profiles(request.json['person'],request.json['experience'],request.json['role'],request.json['ctc'],request.json['expected'])
       db.session.add(obj)
       db.session.commit()
       return single_schema.jsonify(obj)

@app.route("/rest/up/<int:key>",methods=['PUT'])    
def toupdate(key):
    obj=profiles.query.filter_by(id=key).first()
    obj.person=request.json['person']
    obj.role=request.json['role']
    obj.experience=request.json['experience']
    obj.ctc=request.json['ctc']
    obj.expected=request.json['expected']
    db.session.add(obj)

    db.session.commit()
    return single_schema.jsonify(obj)

@app.route("/rest/del/<int:key>",methods=['DELETE'])    
def todelete(key):
    obj=profiles.query.filter_by(id=key).first()
    db.session.delete(obj)
    db.session.commit()
    return single_schema.jsonify(obj)






    @app.route("/new",methods=['GET','POST'])

    def process():
        #db.create_all()
     if not session.get('per'):
        return render_template("login.html")
     else:
        if request.method=='GET':
            return render_template("new.html")
        else:
            p=profiles(request.form['person'],request.form['experience'],request.form['role'],request.form['ctc'],request.form['expected'])    
            db.session.add(p)
            db.session.commit()
            return redirect("/")

    @app.route("/list",methods=['GET']) 
    def listing():
     if not session.get('per'):
         return render_template("login.html")
     else:    
        obj=profiles.query.all()
        return render_template("listing.html",key=obj)    

    @app.route("/up/<int:pk>",methods=['GET','POST'])       
    def update(pk):
     if not session.get('per')   :
         return render_template("login.html")
     else:    
        obj=profiles.query.filter_by(id=pk).first()
        print(obj)
        if request.method=='POST':
            obj.person=request.form['person']
            obj.role=request.form['role']
            obj.experience=request.form['experience']
            obj.ctc=request.form['ctc']
            obj.expected=request.form['expected']
            db.session.add(obj)
            db.session.commit()
            return redirect("/")
        return render_template("update.html",data=obj)

    @app.route("/del/<int:pk>",methods=['GET'])    
    def deleting(pk):
     if not session.get('per'):
         return render_template("login.html")
     else:    
        obj=profiles.query.filter_by(id=pk).first()
        db.session.delete(obj)
        db.session.commit()
        return redirect("/")

    @app.route("/short",methods=['GET','POST'])    
    def shortlisting():
     if not session.get('per'):
         return render_template("login.html")
     else:    
        if  request.method=="POST":
            r=request.form['rol']
            q=request.form['exp']
            print(r)
            print(q)
            # we get one set of resultant record 
            if r!="" and q=="":
                   obj=profiles.query.filter_by(role=r).first()
                   temp1=[]
                   temp1.append(obj)
                   return render_template("choice.html",key=temp1)
            elif r=="" and q!=""    :
                 obj1=profiles.query.filter_by(experience=q).first()
                 print(type(obj1),obj1)
                 temp=[]
                 temp.append(obj1)
                 return render_template("choice.html",key=temp)           

           
            #return render_template("choice.html",key=obj) (we will get typeerror profiles object is not iterable so use temporary array for correction)
            # so use this statement .... return render_template("choice.html",key=temp1)
            ####
            #for getting mutiple set of records which satisfied the condition 
            #pass the obj & no .first() & no temporary array

            #obj=profiles.query.filter_by(role=r)
            #print(type(obj),obj)
            #return render_template("choice.html",key=obj)
        else:
            return render_template ('shortlist.html')    

    @app.route("/",methods=['GET','POST'])
    def logging():
        if request.method=="POST":
            u=request.form['user']
            p=request.form['pass']
            if u=='bhuvan' and p=='123':
               session['per']=u
               return redirect("/list")
            else:
               return render_template("login.html")    
        else:
             return render_template("login.html") 

    @app.route("/out",methods=['GET'])  
    def outting():
        session['per']=None
        return render_template("login.html")       

if __name__=="__main__"       :
    app.run(debug=True)


 