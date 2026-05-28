# Personal Behavior + Fitness + Language Analytics System

## 📌 Project Overview

This project is a personal data-driven system designed to track, analyze, and visualize daily habits across fitness, weight tracking, and language learning.

The system transforms raw daily behaviors into structured datasets and uses them to generate insights about consistency, progress, and long-term behavior patterns.

---

## 🎯 Motivation

I wanted to better understand how my daily habits affect long-term outcomes such as physical health, discipline, and skill development.

This project also serves as a foundation for building systems-thinking and software engineering skills, which I plan to apply later to embedded systems and hardware-based projects (such as Raspberry Pi-based monitoring systems).

---

## ⚙️ System Architecture

The system follows a basic data pipeline:
Data Input → SQLite Database → Data Processing → Streamlit Dashboard

### Components:
- **Data Input Layer:** Manual logging of workouts, weight, and study sessions
- **Database Layer:** SQLite-based structured storage system
- **Processing Layer:** Python-based analytics and calculations
- **Visualization Layer:** Streamlit dashboard for real-time insights

---

## 🧰 Tech Stack

- Python
- SQLite
- Pandas
- Streamlit
- Matplotlib

---

## 📊 Features

- Log daily workouts (type, duration, intensity)
- Track body weight over time
- Record language learning sessions
- Visualize progress trends over time
- Track consistency and streaks
- Generate basic behavioral insights

---

## 🧪 How It Works

1. User inputs daily data (workouts, weight, study sessions)
2. Data is stored in a structured SQLite database
3. Python scripts process and analyze the data
4. Streamlit dashboard displays visual insights
5. System updates dynamically as new data is added

---

## 🗄️ Database Structure

### workouts
- id
- date
- type
- duration
- intensity

### weight
- id
- date
- weight

### study_sessions
- id
- date
- language
- minutes

---

## 🚧 Challenges Faced

- Designing a clean database schema for multiple data types
- Handling inconsistent or missing data entries
- Structuring time-series data for visualization
- Learning how to connect backend data to a live dashboard

---

## 📈 Insights & Learnings

- Importance of consistency in data collection
- Value of simple system design over complex features
- How structured data can reveal behavioral patterns
- Tradeoffs between simplicity and scalability

---

## 🔮 Future Improvements

- Mobile-friendly data entry system
- Integration with wearable fitness data (Apple Health / Fitbit API)
- Predictive modeling for habit consistency
- Automated data collection
- Expansion into a full personal analytics platform

---

## 🎥 Demo

Will include:
- Screenshots of dashboard
- Short demo video (30–90 seconds)

---

## 🧠 Project Significance

This project demonstrates early-stage systems engineering skills, including:
- data pipeline design
- database architecture
- software modularization
- behavioral data modeling

It serves as a foundation for future embedded systems and hardware-software integration projects.

---

## 👤 Author

Colin Williams

Background:
- Psychology (B.A.)
- Interest in computer systems, hardware, and behavioral analytics
- Currently transitioning into engineering-focused graduate study

---

## 📌 Status

🚧 In active development 
