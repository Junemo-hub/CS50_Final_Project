# ESG Evaluation App (CS50 Final Project)

#### Video Demo: https://youtu.be/Tx30U1eAJ0I

This is a Flask-based web app that evaluates a user's ESG (Environmental, Social, Governance) profile based on their responses to a survey. It's my final project for Harvard's [CS50x](https://cs50.harvard.edu/x), where I wanted to build something that combined backend logic with real-time feedback and simple data visualization.

---

## How to Run Locally

1. Clone the repository.
2. Create a virtual environment.
3. Install dependencies: pip install -r requirements.txt
4. Run the app: Visit `http://127.0.0.1:5000` in your browser.


---

## Features

- **User login system**  
Users can sign up, log in, and securely manage their sessions.

- **Survey-based ESG scoring**  
The app asks a set of multiple-choice questions across environmental, social, and governance categories. Answers are scored based on ESG principles.

- **Visualized results**  
Scores are shown as donut charts using Chart.js, helping users quickly understand their strengths and weaknesses across ESG components.

- **Evaluation storage**  
Each result is saved in the database, allowing users to track progress over time (optional feature for future enhancements).

- **Flash messages & error handling**  
Feedback is provided via Flask flash messages for login errors, logout confirmation, and survey submission.

---

## Tech Stack

- **Frontend**: HTML, CSS (custom), JavaScript (Chart.js via CDN)
- **Backend**: Python (Flask), Jinja2 templating
- **Database**: SQLite using SQLAlchemy ORM
- **Other**: Flask sessions, Werkzeug password hashing, flash messaging

---

## File Overview

project/
│
├── app.py # Main Flask app with all route logic
├── models.py # SQLAlchemy models (User, Survey, Evaluation)
├── templates/ # HTML templates rendered with Jinja2
│ ├── index.html # Main landing page with login status
│ ├── login.html # Login form and flash messages
│ ├── register.html # Signup form with password confirmation
│ ├── survey.html # Survey form for ESG questions
│ └── result.html # Donut chart results using Chart.js
└── static/ # (Unused for now, reserved for future CSS/JS files)


---

## Design Decisions

- No Bootstrap or external UI libraries were used, to keep the frontend lightweight and focused on core functionality.
- Each answer of "Yes" scores positively; "No" is neutral; "I don't know" is scored as 0, simulating real ESG risks from lack of awareness.
- After survey submission, previous responses are wiped to avoid duplication before inserting a new record.
- Flash messages enhance user feedback and session control (login/logout alerts, error notices).
- Donut charts provide visual clarity while maintaining minimal layout impact.

---

## What I Learned

- How to structure and build a full-stack Flask web application
- Handling user authentication, session state, and flash messaging
- Database design using SQLAlchemy and managing foreign key relationships
- Frontend integration with Python backend using Jinja2 and Chart.js
- Managing user inputs securely and storing evaluation results persistently
- Debugging UI feedback issues, especially with session/flash behavior

---

## Use of AI Tools

Some structural debugging and UI behavior analysis were supported using ChatGPT, specifically for improving login flow flash messages. All core logic and implementation were written and tested independently.

---

## Project Link

[GitHub Repository](https://github.com/Junemo-hub/CS50_Final_Project/)

---

## Timeline

- Project started: April 2025  
- Final video & submission: June 2025

---

## Contact

📫 junemo.moon@gmail.com  
🌐 Seoul, South Korea  
