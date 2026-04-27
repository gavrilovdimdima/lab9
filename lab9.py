# from flask import Flask, render_template

# app = Flask('Task List')

# tasks = []

# @app.route('/')
# def main():
#     return render_template('index.html', my_tasks=tasks)




# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///workplaces.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Workplace(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    term = db.Column(db.Integer, nullable=False)


@app.route("/")
def index():
    workplaces = Workplace.query.all()

    total_term = sum(place.term for place in workplaces)
    years = total_term // 12
    months = total_term % 12

    return render_template(
        "index.html",
        workplaces=workplaces,
        total_term=total_term,
        years=years,
        months=months
    )


@app.route("/add", methods=["POST"])
def add_workplace():
    data = request.get_json()

    workplace = Workplace(
        company=data["company"],
        term=int(data["term"])
    )

    db.session.add(workplace)
    db.session.commit()

    return jsonify({"status": "ok"})


@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_workplace(id):
    workplace = Workplace.query.get_or_404(id)

    db.session.delete(workplace)
    db.session.commit()

    return jsonify({"status": "ok"})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)