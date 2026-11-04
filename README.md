# Microservices Assignment

**Student:** Ayesha Memon  
**Project:** Microservices Assignment  
**Technologies:** Python, Flask, SQLite, Streamlit, PyJWT

## Project Overview

This project contains three tasks related to Microservices and API development.

### Task 1: Student Management API

A Student Management System developed using Flask, SQLite, and Streamlit.

**Features:**
- Add student records.
- View all students.
- Update student records.
- Delete student records.

**Technologies:** Flask, SQLite, Streamlit, Python.

**How to Run:**

1. Open the Task1 folder.
2. Run the Flask API:

   `python App.py`

3. Open another terminal and run:

   `streamlit run streamlit_app.py`

### Task 2: API Key Generation and Sharing

A protected API developed using Flask.

**Features:**
- Generate three API keys for three consumers.
- Validate API keys.
- Reject requests with missing API keys.
- Reject requests with invalid API keys.
- Allow access to consumers with valid API keys.

**API Endpoint:**

`GET /api/data`

**Header:** `X-API-Key`

**How to Run:**

1. Open the Task2 folder.
2. Run:

   `python app.py`

3. Test the API using cURL.

### Task 3: Authentication and Authorization Using JWT

An employee authentication system developed using Flask and PyJWT.

**Features:**
- Employee login.
- Admin login.
- JWT token generation.
- Token verification.
- Role-based authorization.
- Separate employee and admin access.

**API Endpoints:**

- `POST /login`
- `GET /employee`
- `GET /admin`

**Demo Login Credentials:**

Employee:
- Username: `emp1`
- Password: `123`

Admin:
- Username: `admin1`
- Password: `admin123`

**How to Run:**

1. Open the Task3 folder.
2. Run:

   `python app.py`

3. Test login and protected endpoints using PowerShell.

## Project Structure

```text
Microservice_assignment/
│
├── Task1/
│   ├── App.py
│   └── streamlit_app.py
│
├── Task2/
│   └── app.py
│
├── Task3/
│   └── app.py
│
├── .gitignore
└── README.md
```

## Installation

Install the required Python libraries:

```bash
pip install Flask streamlit requests pandas PyJWT
```

## GitHub Repository

https://github.com/ayeshamemon1327-blip/Microservice-Assignment

## Note

This project is developed for educational and demonstration purposes. The credentials and security configuration are examples and should not be used in production systems.