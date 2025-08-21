import csv
from pymongo import MongoClient

# MongoDB Atlas connection
client = MongoClient("mongodb+srv://survey_user:StrongPass123@healthsurverycluster.mdxv8kp.mongodb.net/?retryWrites=true&w=majority&appName=HealthSurveryCluster")
db = client["survey_db"]
collection = db["responses"]

EXPENSE_CATEGORIES = ["Utilities", "Entertainment", "School Fees", "Shopping", "Healthcare"]

all_responses = list(collection.find())

with open("survey_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
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

print("Export complete! survey_data.csv created.")
