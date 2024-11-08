from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route("/about")
def about():
    return"<h1>Good Evening</h1>"

@app.route("/api")
def api():
    return "<p style='color:red;'>,Vignesh</p>"

if __name__ == '__main__':
    app.run(debug=True)
