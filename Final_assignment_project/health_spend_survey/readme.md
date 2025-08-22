Project: Flask Survey App with MongoDB, CSV Export, and AWS Deployment
1. Overview

This project is a Flask-based web application that collects user demographic and financial data, stores it in MongoDB, processes and exports the data as CSV files, visualizes insights in Jupyter Notebook, and is ready for deployment on AWS Elastic Beanstalk.

2. Features

Web App with Flask

Collects user information: Name, Age, Gender, Income.

Includes expense categories with checkboxes and amount fields (Utilities, Entertainment, School Fees, Shopping, Healthcare).

MongoDB Integration

Stores all user submissions in a MongoDB collection.

Data Export

/export route → generates a CSV file and downloads it instantly.

/save_csv route → saves a timestamped CSV file inside a local data/ folder.

Data Processing & Visualization

Python User class for organizing user data.

Jupyter Notebook to:

Identify ages with the highest income.

Visualize gender distribution across expense categories (fixed to show Male, Female, Other consistently).

Export all charts as PNG images (saved inside a charts/ folder).

AWS Deployment (Prepared)

Configured Procfile with web: gunicorn app:app.

Ready for deployment to Elastic Beanstalk.

3. Tech Stack

Backend: Flask (Python 3.11)

Database: MongoDB

Visualization: Matplotlib / Seaborn (Jupyter Notebook)

Deployment: AWS Elastic Beanstalk (Gunicorn as WSGI server)

4. Project Structure
flask-survey-app/
│
├── app.py                  # Main Flask app with routes
├── forms.py                # Flask-WTF form definitions
├── templates/
│   └── form.html           # HTML form for survey
├── user.py                 # User class to structure CSV export
├── data/                   # Folder where timestamped CSV files are saved
├── charts/                 # Folder where PNG charts are exported
├── notebook.ipynb          # Jupyter notebook for data visualization
├── Procfile                # For AWS Elastic Beanstalk (Gunicorn config)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

5. Installation & Local Setup
git clone <repo_url>
cd flask-survey-app
python -m venv venv
source venv/bin/activate      # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
flask run

6. Routes

GET / → Display form

POST / → Submit user data to MongoDB

GET /export → Download CSV file directly

GET /save_csv → Save CSV file in data/ folder

7. Data Visualization (Jupyter)

Run notebook.ipynb to:

Load CSV data into pandas DataFrame.

Clean up gender labels and ensure Male/Female/Other appear.

Create boxplots of expense categories vs gender.

Export charts automatically to charts/ folder for presentation.

8. Deployment to AWS

Install EB CLI: pip install awsebcli

Initialize app: eb init -p python-3.11 flask-survey-app --region us-east-2

Create environment: eb create flask-env

Deploy updates: eb deploy

Open app: eb open

Issue with aws-deployment as my aws account has an issue and would take some days to resolve.