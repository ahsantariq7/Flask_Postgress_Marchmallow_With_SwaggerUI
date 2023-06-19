from flask import render_template  # Remove: import Flask

from src.app import create_app
from src.models import Person

# app = connexion.App(__name__, specification_dir="./")


connex_app = create_app()

connex_app.add_api("swagger.yml")
app = connex_app.app


@app.route("/")
def home():
    people = Person.query.all()
    return render_template("home.html", people=people)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
