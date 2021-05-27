from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key="keep it safe"
@app.route("/")



def counter():
    if "counter" in session:
        session['counter']=session.get('counter')+1
    else:
        session['counter']=1
    return "visit = {}".format (session.get('counter'))
@app.route("/destroy")
def destroy():
    session.clear()
    return redirect("/")
if __name__=="__main__":
    app.run(debug=True)