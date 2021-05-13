from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")

if __name__ == "__main__":
    app.run(debug=True)