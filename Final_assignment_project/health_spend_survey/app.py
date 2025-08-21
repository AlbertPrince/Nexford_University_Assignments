from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, DecimalField, StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange, InputRequired
from flask_bootstrap import Bootstrap5
from decimal import Decimal
from pymongo import MongoClient

from flask import send_file
import csv
import io

app = Flask(__name__)
app.secret_key = "change_this_secret_key"  
bootstrap = Bootstrap5(app)

client = MongoClient("mongodb+srv://survey_user:StrongPass123@healthsurverycluster.mdxv8kp.mongodb.net/?retryWrites=true&w=majority&appName=HealthSurveryCluster")
db = client["survey_db"]
collection = db["responses"]

EXPENSE_CATEGORIES = ["Utilities", "Entertainment", "School Fees", "Shopping", "Healthcare"]

def create_survey_form():
    class DynamicSurveyForm(FlaskForm):
        name = StringField("Name", validators=[InputRequired()])
        age = IntegerField("Age", validators=[DataRequired(), NumberRange(min=0, max=120)])
        gender = SelectField("Gender", choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])
        income = DecimalField("Total Income ($)", validators=[DataRequired()])
        submit = SubmitField("Submit")

    for category in EXPENSE_CATEGORIES:
        setattr(
            DynamicSurveyForm,
            category,
            DecimalField(
                f"{category} ($)", 
                validators=[NumberRange(min=0)], 
                places=2, 
                default=Decimal("0")
            )
        )
    return DynamicSurveyForm()

@app.route("/", methods=["GET", "POST"])
def index():
    form = create_survey_form()
    if form.validate_on_submit():
        # Basic user info
        data = {
            "name": form.name.data,
            "age": form.age.data,
            "gender": form.gender.data,
            "income": float(form.income.data) if form.income.data is not None else 0.0,
            "expenses": {}
        }

        # Handle expenses: only store amounts if the checkbox is checked
        for category in EXPENSE_CATEGORIES:
            checked = request.form.get(f"{category}_check")  # returns 'on' if checked
            amount = request.form.get(f"{category}_amount")  # string from input
            if checked and amount:
                try:
                    data["expenses"][category] = float(amount)
                except ValueError:
                    data["expenses"][category] = 0.0  # fallback if input invalid

        # Save to MongoDB
        collection.insert_one(data)

        return "<h3>Form submitted successfully and stored in MongoDB!</h3>"

    return render_template("form.html", form=form)


@app.route("/export")
def export_csv():
    all_responses = list(collection.find())

    output = io.StringIO()
    writer = csv.writer(output)

    header = ["name", "age", "gender", "income"] + EXPENSE_CATEGORIES
    writer.writerow(header)

    for doc in all_responses:
        row = [
            doc.get("name"),
            doc.get("age"),
            doc.get("gender"),
            doc.get("income")
        ] + [doc["expenses"].get(cat, 0) for cat in EXPENSE_CATEGORIES]
        writer.writerow(row)

    output.seek(0)

    return send_file(
        io.BytesIO(output.getvalue().encode()),
        mimetype="text/csv",
        as_attachment=True,
        download_name="survey_data.csv"
    )


if __name__ == "__main__":
    app.run(debug=True)
