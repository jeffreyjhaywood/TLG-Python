from flask import Flask, render_template
import scrapetest


app = Flask(__name__)


@app.route("/")
def display_tv_details():
    tv_li = scrapetest.lookup_gaming_tvs()
    return render_template("index.html", tvs=tv_li)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
