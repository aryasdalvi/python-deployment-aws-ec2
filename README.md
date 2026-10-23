# Python Application Deployment on AWS EC2

## Introduction

This project demonstrates deploying a Python web application on an AWS EC2 instance running Amazon Linux. The application, named **Radhe Shyam**, is an online shop inspired by Shri Krishna and Radha Rani. The project covers Python installation, GitHub repository cloning, virtual environment creation, dependency installation, and application execution using Gunicorn.

## Objectives

- Install Python and pip on AWS EC2.
- Clone the application from GitHub.
- Create and activate a Python virtual environment.
- Install dependencies from `requirements.txt`.
- Run the application on port 5000.
- Run the application in the background using Gunicorn.

## Architecture

**Application Flow:**

<img width="1774" height="887" alt="image" src="https://github.com/user-attachments/assets/c22cb496-2baf-4fa3-8e83-fae90d2a885e" />


User / Browser → Internet → AWS EC2 → Python Application → Gunicorn → Port 5000

The application runs on an Amazon Linux EC2 instance. Python executes the application code, pip installs dependencies, and Gunicorn serves the application on port 5000.



## Technologies Used

| Technology | Purpose |
|---|---|
| AWS EC2 | Cloud server hosting |
| Amazon Linux | Operating system |
| Python 3 | Application runtime |
| pip | Dependency management |
| Git | Cloning the application repository |
| Virtual Environment | Python dependency isolation |
| Gunicorn | Python WSGI server |

## Deployment Steps

### 1. Update the System

```bash
sudo yum update
```

### 2. Install Python

```bash
sudo yum install python3 -y
python --version
pip --version
sudo yum install pip -y
```

### 3. Clone the Application from GitHub

```bash
git clone <GitHub-Repository-URL>
```

Check the application files:

```bash
ls
```

The project contains `app.py` and `requirements.txt`.

### 4. Navigate to the Project Directory

```bash
cd /home/ec2-user/python
```

### 5. Create a Virtual Environment

```bash
sudo python3 -m venv myenv
```

### 6. Activate the Virtual Environment

```bash
source myenv/bin/activate
```

### 7. Install Dependencies

```bash
sudo pip install -r requirements.txt
```

### 8. Run the Python Application

```bash
python3 app.py
```

### 9. Run the Application in the Background

```bash
gunicorn --bind 0.0.0.0:5000 app:app --daemon
```

### 10. Access the Website

**Public IP:** `54.225.23.109`

**Website URL:** http://54.225.23.109:5000

The deployed website displays the Radhe Shyam online shop and its collection of products inspired by Shri Krishna and Radha Rani.

## Screenshots

- Terminal:
  <img width="1448" height="524" alt="Screenshot 2026-10-23 213001" src="https://github.com/user-attachments/assets/977d6164-ba21-4398-9984-8e417868e7df" />

- Application running on EC29 (A.linux):
  <img width="1832" height="610" alt="Screenshot 2026-10-23 212940" src="https://github.com/user-attachments/assets/64e216cd-4a75-479d-be7c-677c239893e1" />

- Deployed Radhe Shyam Python website:
  <img width="1894" height="1024" alt="Screenshot 2026-10-23 211322" src="https://github.com/user-attachments/assets/96118a19-f505-489d-9777-158459006912" />



## Key Learnings

- AWS EC2 and Linux administration
- Python and pip installation
- GitHub repository cloning
- Virtual environment creation and activation
- Dependency installation using `requirements.txt`
- Running a Python application using Gunicorn
- Accessing a deployed application through a public IP and port


## Summary

Deployed the Radhe Shyam Python web application on AWS EC2. Installed Python, cloned the application repository, created a virtual environment, installed dependencies, and used Gunicorn to run the application on port 5000.

