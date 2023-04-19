from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
@app.route('/play/<int:number>')
@app.route('/play/<color>')
@app.route('/play/<color>/<int:number>')
def index(number=3,color="blue"):
    return render_template("index.html",number=number,color=color)
if __name__=="__main__":
    app.run(debug=True)
