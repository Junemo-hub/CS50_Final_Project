# ESG Evaluation App (CS50 Final Project)

This is a Flask-based web app that evaluates a user's ESG (Environmental, Social, Governance) profile based on their responses to a survey. It's my final project for Harvard's [CS50x](https://cs50.harvard.edu/x), where I wanted to build something that combined backend logic with real-time feedback and simple data visualization.

---

## Features

- **User login system**  
  Users can sign up and log in to access their ESG evaluation.

- **Survey-based scoring**  
  The app asks a series of questions across environmental, social, and governance topics, and calculates a score based on the answers.

- **Chart-based results**  
  Scores are visualized in a compact donut chart so users can quickly see how they did in each category.


---

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript, Chart.js  
- **Backend**: Flask (Python), Jinja2  
- **Database**: SQLite with SQLAlchemy  
- **Other**: Flask session management, password hashing with Werkzeug

---

## Project Status

The main flow — survey, scoring, and result visualization — is complete.  
- I'm currently adding score history so logged-in users can see previous evaluations.
+ The core survey and result flow is complete. Future improvements may include result history or better survey analytics.


---

## Folder Overview
```
project/
│
├── app.py
├── models.py
├── templates/
│ ├── index.html
│ ├── login.html
│ ├── register.html
│ ├── result.html
│ └── survey.html
├── static/
└── README.md
```

---

## What I Learned

- How to build and structure a Flask app
- Processing form inputs and storing them in a database
- Handling authentication and session logic
- Connecting Python logic to frontend charts

---

## Project Link

[[GitHub Repository]](https://github.com/Junemo-hub/CS50_Final_Project/)

---

## Timeline

- Project started: April 2025  
- CS50 final submission: May 2025  
- Score history feature: in progress

---

## Contact

If you have any questions or feedback:  
📫 junemo.moon@gmail.com

