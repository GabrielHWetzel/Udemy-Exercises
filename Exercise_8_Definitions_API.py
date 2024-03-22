from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("Home.html")


@app.route("/api/v1/<word>")
def api(word):
    definition = word.upper()
    result = {"word": word,
              "definition": definition}
    return result


if __name__ == "__main__":
    app.run(debug=True)
