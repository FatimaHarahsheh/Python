from flask import Flask ,render_template,request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/result',methods=["post"])
def result():
   name=request.form["fname"]
   location=request.form["location"]
   Language=request.form["Language"]
   comment=request.form["comment"]
   return render_template("result.html",name=name,location=location,Language=Language,comment=comment)
if __name__ == "__main__":

    app.run(port=5001,debug=True)
