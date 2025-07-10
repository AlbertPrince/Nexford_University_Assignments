import random

first_names_male = ["Kwesi", "Stiles", "Peter", "David", "James", "Stiles", "Scott", "Richard", "Thomas", "Bruce"]
first_names_female = ["Afia", "Adjeley", "Leticia", "Wendy", "Josephine", "Blessing", "Holly", "Sarah", "Karen", "Nancy"]
last_names = ["Nunoo", "Lartey", "Anokye", "Parker", "Quill", "Mensah", "Gbotsu", "Wayne", "McCall", "Stilinski"]

workers = []
for i in range(1, 401):
    gender = random.choice(["Male", "Female"])
    if gender == "Male":
        first_name = random.choice(first_names_male)
    else:
        first_name = random.choice(first_names_female)
    last_name = random.choice(last_names)
    name = f"{first_name} {last_name}"
    worker_id = f"W{i:04d}"
    salary = random.randint(5000, 32000)
    workers.append({
        "id": worker_id,
        "name": name,
        "gender": gender,
        "salary": salary
    })

for worker in workers:
    try:
        level = ""
        if 10000 < worker["salary"] < 20000:
            level = "A1"
        if worker["gender"] == "Female" and 7500 < worker["salary"] < 30000:
            level = "A5-F"
        print(f"Payment Slip for {worker['name']} (ID: {worker['id']})")
        print(f"Gender: {worker['gender']}")
        print(f"Salary: ${worker['salary']}")
        print(f"Employee Level: {level if level else 'N/A'}")
        print("-" * 40)
    except KeyError as e:
        print(f"Missing key in worker data: {e}")
    except TypeError as e:
        print(f"Type error in worker data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
