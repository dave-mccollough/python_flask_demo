from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():    
    return render_template("index.html")

@app.route("/code.html")
def publish_code():
    return render_template("code.html")

@app.route("/docker.html")
def publish_docker():
    return render_template("docker.html")


if __name__ == '__main__':
    app.run(debug=True)
        