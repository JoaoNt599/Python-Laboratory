from flask import Flask


app = Flask(__name__)


@app.route("/")
def homepage():
    return 'Flask Page'


if __name__ == "__main__":
    app.run(debug=True)