from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello():
    name="harry"
    return render_template('index.html')

 

@app.route("/about")
def harry():
    name="harry"
    return render_template("about.html",name2=name)


@app.route('/bootstrap')
def bootstrap():
    return render_template("bootstrap.html")

app.run()