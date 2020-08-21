from flask import Flask, render_template
import sitestealer as s


app = Flask(__name__)


@app.route("/")
def render_stolen_site():
    try:
        return render_template("stolensite.html")
    except:
        return "Could not render site"


if __name__ == "__main__":
    s.steal_site()
    app.run(host="0.0.0.0", port=2224)
