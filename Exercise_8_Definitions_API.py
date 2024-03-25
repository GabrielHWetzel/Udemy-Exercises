import pandas
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("Home.html")


@app.route("/api/v1/<word>")
def api(word):
    df = pandas.read_csv("Files/dictionary.csv")
    definition = df.loc[df["word"] == word]["definition"].squeeze()

    result = {"word": word,
              "definition": definition}
    return result


if __name__ == "__main__":
    app.run(debug=True)
