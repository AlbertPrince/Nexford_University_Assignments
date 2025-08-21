from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    age = request.form.get("age")
    gender = request.form.get("gender")
    income = request.form.get("income")

    expenses = {}
    categories = ["utilities", "entertainment", "school", "shopping", "healthcare"]
    for category in categories:
        if request.form.get(f"expense_{category}"):
            amount = request.form.get(f"amount_{category}", 0)
            expenses[category] = float(amount) if amount else 0.0



    print("New submission: ")
    print(f"Name: {name}, Age: {age}, Gender: {gender}, Income: {income}, Expenses: {expenses}")

    return f"<h2> Thanks for submitting, {gender} aged {age}!</h2>"



if __name__ == "__main__":
    app.run(debug=True)