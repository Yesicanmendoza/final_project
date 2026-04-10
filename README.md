# 🐾 The Pet Tracker

A full-stack web application that helps users find lost pets by matching them with rescued animals using a custom algorithm based on pet characteristics and geographic proximity.

## 🔍 Project Overview

This app connects people who have lost a pet with those who have rescued one. Users register either a lost or rescued pet, and the matching algorithm compares key characteristics — returning the most likely matches within a 30-mile radius.

**Core matching criteria:**
- Animal type, breed, color, and gender
- Date lost vs. date rescued
- Geographic distance (≤ 30 miles between loss and rescue location)

The algorithm also accounts for variations in user input, including inconsistent capitalization, punctuation, and missing fields.

---

## ✨ Features

- User authentication with encrypted passwords (register, login, logout)
- Pet registration for both lost and rescued animals
- Automated matching algorithm with fuzzy input handling
- Match results display with pet photo and owner contact info
- Option to mark a pet as found, removing both matched records from the database
- Interactive map integration via Google Maps API
- Image upload and storage via Cloudinary API

---


## 📸 App Screenshots

### Homepage
The homepage displays how the app works and tips for lost or rescued pet owners. 
Users must create an account and log in to access the full navigation menu.
![Homepage](https://user-images.githubusercontent.com/80706744/182918991-71e85210-e275-4bc3-bf49-7cbee431fb9b.PNG)

### Pet Registration
Register a lost or rescued pet by entering key characteristics. The database includes 
30 pre-loaded rescued dogs and 30 cats in the Sacramento area (rescued April 1, 2022).
![Pet registration](https://user-images.githubusercontent.com/80706744/182919162-457d99e7-5f94-48f7-8453-2af39a869fa6.PNG)

### Search for a Match
Access pet search from the navigation menu or automatically after registration. 
Click on your pet's name to start or stop the search.
![Looking a match](https://user-images.githubusercontent.com/80706744/182919248-3fb125a1-8798-40c9-b7e3-167ba32d1323.PNG)

### Match Results
View matched pets with their photo and owner contact email. If you found your pet, 
submit the matched pet's ID to remove both records from the database.
![Matched found](https://user-images.githubusercontent.com/80706744/182919331-d18efff2-3b6c-40e7-9b98-978cd4e6fc06.PNG)


## 🛠️ Tech Stack

| Layer | Technologies |
|---|---|
| **Backend** | Python, Flask, SQLAlchemy |
| **Frontend** | JavaScript, React, HTML, CSS, Bootstrap |
| **Templating** | Jinja2 |
| **Async** | AJAX |
| **Database** | PostgreSQL (via SQLAlchemy ORM) |
| **APIs** | Google Maps API, Cloudinary API |

---

## 🚀 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/Yesicanmendoza/final_project.git
cd final_project

# Create and activate virtual environment
python3 -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
# Create a .env file with your Google Maps API key and Cloudinary credentials

# Run the app
python server.py
```

---

## 🧪 Testing the App

The database is pre-loaded with **30 rescued dogs** and **30 rescued cats** in the Sacramento area, all rescued on **April 1, 2022**.

To test matching:
- Register a lost pet with a loss date **on or before April 1, 2022**
- Use a Sacramento-area zip code
- The algorithm will return matches within 30 miles

You can also register both a lost and a rescued pet manually and verify they match each other.

---

## 📁 Project Structure

```
final_project/
├── server.py            # Flask routes and app entry point
├── model.py             # SQLAlchemy database models
├── crud.py              # Database CRUD operations
├── data.py              # Data processing logic
├── seed_database.py     # Database seed file (30 dogs + 30 cats)
├── data/
│   ├── pets_data.py     # Pet data definitions
│   └── bS_get_data.py  # Data retrieval scripts
├── static/
│   ├── look_the_pet.jsx # React component for pet search
│   ├── pet_info.js      # Pet information scripts
│   ├── styles.css       # Stylesheet
│   └── img/             # Image assets
└── templates/           # Jinja2 HTML templates
```

---

## 👩‍💻 About

Built as the capstone project for the **Hackbright Academy** Software Engineering program (2022).  
Developed by **Yesica Mendoza** — [LinkedIn](https://www.linkedin.com/in/yesicanmendoza) | [GitHub](https://github.com/Yesicanmendoza)
 


