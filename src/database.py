import sqlite3
from datetime import datetime

DB_NAME = "data/habit_data.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = connect()
    cur = conn.cursor()

    # Workouts table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS workouts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        type TEXT,
        duration INTEGER,
        intensity INTEGER
    )
    """)

    # Weight table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS weight (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        weight REAL
    )
    """)

    # Study sessions table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS study_sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        language TEXT,
        minutes INTEGER
    )
    """)

    conn.commit()
    conn.close()


def init_db():
    create_tables()
def add_workout(date, workout_type, duration, intensity):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO workouts (date, type, duration, intensity)
        VALUES (?, ?, ?, ?)
    """, (date, workout_type, duration, intensity))

    conn.commit()
    conn.close()


def add_weight(date, weight):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO weight (date, weight)
        VALUES (?, ?)
    """, (date, weight))

    conn.commit()
    conn.close()


def add_study_session(date, language, minutes):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO study_sessions (date, language, minutes)
        VALUES (?, ?, ?)
    """, (date, language, minutes))

    conn.commit()
    conn.close()
