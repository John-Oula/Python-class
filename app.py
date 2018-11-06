from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("HOME.html")
@app.route('/Login')
def log_in():
    return render_template("LOG IN.html")
@app.route('/contacts')
def log_in1():
    return render_template("contacts.html")
@app.route('/designs')
def log_in2():
    return render_template("designs.html")


if __name__ == '__main__':
    app.run()
