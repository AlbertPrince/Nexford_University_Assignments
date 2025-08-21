from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, DecimalField, StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange, InputRequired
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.secret_key = "change_this_secret_key"  # required for CSRF
bootstrap = Bootstrap5(app)

EXPENSE_CATEGORIES = ["Utilities", "Entertainment", "School Fees", "Shopping", "Healthcare"]


# ---- Define the form ----
class SurveyForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    age = IntegerField("Age", validators=[DataRequired(), NumberRange(min=0, max=120)])
    gender = SelectField("Gender", choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])
    income = DecimalField("Total Income ($)", validators=[DataRequired()])
    # We'll handle expenses dynamically later
    submit = SubmitField("Submit")

# ---- Define routes ----
@app.route("/", methods=["GET", "POST"])
def index():
    form = SurveyForm()
    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        gender = form.gender.data
        income = form.income.data
        
        expenses = {}
        for category in EXPENSE_CATEGORIES:
            amount = request.form.get(category)
            if amount:
                expenses[category] = amount

        print(f"Name={name}, Age={age}, Gender={gender}, Income={income}, Expenses={expenses}")
        return "<h3>Form submitted successfully!</h3>"
    return render_template("form.html", form=form, categories=EXPENSE_CATEGORIES)

if __name__ == "__main__":
    app.run(debug=True)
