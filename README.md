# VulnOps - Vulnerability Operations Center

**VulnOps** is a web-based application designed to help security teams and analysts track, manage, and monitor vulnerabilities across an organization’s infrastructure. The app provides a dashboard for overseeing open vulnerabilities, adding new ones, and generating reports on their status and severity.

## Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Authentication**: Role-based login system for Admins and Analysts.
- **Vulnerability Management**: Add and manage vulnerabilities, with fields for CVE ID, severity, and description.
- **Semi-Automatic Qualys Import**: Import vulnerabilities from your Qualys account
- **Dashboard**: View open vulnerabilities with filtering based on severity and status.
- **User Management**: Role-based access control with separate views for admins and analysts.
- **Real-Time Data**: Keep track of open vulnerabilities and monitor them in real time.
- **Logging & Auditing**: Track updates to vulnerabilities for accountability.

## Screenshots

![Dashboard Example](#)  
*Add a screenshot of the dashboard here*

![Add Vulnerability](#)  
*Add a screenshot of the add vulnerability page here*

## Tech Stack

- **Frontend**: HTML, CSS (with Bootstrap for styling)
- **Backend**: Flask (Python) as the web framework
- **Database**: SQLite (can be replaced with PostgreSQL, MySQL, etc.)
- **User Authentication**: Flask-Login
- **Forms**: Flask-WTF
- **Charting/Visualization**: Chart.js or Plotly for vulnerability trends (Optional)
- **Other Tools**: SQLAlchemy for database ORM, Flask-Migrate for handling database migrations

## Installation

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/medxhub/vulnops.git
   cd vulnops
   ```
   
2. **Set up virtual environment**:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Set up the database**:

Initialize the database with migrations:

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

5. **Run the application**:

```bash
python app.py
```

6. **Access the application**:

Open your browser and go to:

http://127.0.0.1:5000/

