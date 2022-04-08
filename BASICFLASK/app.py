from flask import Flask,render_template
app=Flask(__name__)


@app.route("/")
def func():
    return "<h4>welcome to FLASK</h4>"

@app.route("/ul")
def func2():
    return "<ul><li>python</li><li>django</li><li>flask</li></ul>" 

@app.route("/page1")
def func3():
    return render_template('first.html',data="Bhuvan")

@app.route("/page2")
def func4():
    return render_template('second.html')


@app.route("/page3/<val>")    
def func5(val):
    return render_template("first.html",data=val)

@app.route("/page4/<int:val>")
def func6(val):
    return render_template("first.html",data=val*val*val)


if  __name__=="__main__":
     app.run(debug=True,port=1000)    