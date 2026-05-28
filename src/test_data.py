from database import init_db, add_workout, add_weight, add_study_session

init_db()

add_workout("2026-05-28", "pushups", 20, 7)
add_weight("2026-05-28", 175)
add_study_session("2026-05-28", "spanish", 30)

print("Test data inserted successfully")
