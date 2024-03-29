from flask import Flask
app = Flask(__name__)
@app.route("/")    
def hello_world():
    return 'Hello World!'
@app.route("/dojo") 
def dojo():
    return 'Dojo!'

@app.route("/say/flask")
def hi():
    return "hi flask !"

@app.route('/say/<name>') 
def hello(name):
    print(name)
    return "hi, " + name
@app.route('/repeat/<num>/<word>') 
def repeat(num,word):
    return (word* int(num))
if __name__=="__main__":
    app.run(debug=True)