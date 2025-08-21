from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, DecimalField, StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange, InputRequired
from flask_bootstrap import Bootstrap5
from decimal import Decimal
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "change_this_secret_key"  # required for CSRF
bootstrap = Bootstrap5(app)

client = MongoClient("mongodb+srv://survey_user:StrongPass123@healthsurverycluster.mdxv8kp.mongodb.net/?retryWrites=true&w=majority&appName=HealthSurveryCluster")
db = client["survey_db"]
collection = db["responses"]

EXPENSE_CATEGORIES = ["Utilities", "Entertainment", "School Fees", "Shopping", "Healthcare"]

# ---- Form factory ----
def create_survey_form():
    class DynamicSurveyForm(FlaskForm):
        name = StringField("Name", validators=[InputRequired()])
        age = IntegerField("Age", validators=[DataRequired(), NumberRange(min=0, max=120)])
        gender = SelectField("Gender", choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])
        income = DecimalField("Total Income ($)", validators=[DataRequired()])
        submit = SubmitField("Submit")

    # Dynamically add expense fields
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

# ---- Routes ----
@app.route("/", methods=["GET", "POST"])
def index():
    form = create_survey_form()
    if form.validate_on_submit():
        data = {
            "name": form.name.data,
            "age": form.age.data,
            "gender": form.gender.data,
            "income": float(form.income.data) if form.income.data is not None else 0.0,
            "expenses": {cat: float(getattr(form, cat).data) for cat in EXPENSE_CATEGORIES}
        }
        collection.insert_one(data)  # Save to MongoDB
        return "<h3>Form submitted successfully and stored in MongoDB!</h3>"
    return render_template("form.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
