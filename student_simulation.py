import random
import pandas as pd
import numpy as np

# List of courses from the astronomy curriculum
course_list = [
    "A101", "A102", "A103",
    "A201", "A202", "A203",
    "A301", "A302", "A303",
    "A401", "A402"
]

# Possible interests students can have
interest_areas = [
    "Stellar Astrophysics", "Galactic Astronomy", "Planetary Science", 
    "Cosmology", "Astrobiology", "Observational Techniques"
]


grade_scale = {
    "A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0
}

students = []

for student_id in range(1, 101):  # 100 students
    num_courses_taken = random.randint(3, 8)  # Each student completed 3–8 courses
    completed = random.sample(course_list, num_courses_taken)
    
    grades = {}
    total_points = 0
    for course in completed:
        letter = random.choices(list(grade_scale.keys()), weights=[0.3, 0.3, 0.2, 0.1, 0.1])[0]
        grades[course] = letter
        total_points += grade_scale[letter]
    
    gpa = round(total_points / num_courses_taken, 2)

    interests = random.sample(interest_areas, k=random.randint(1, 2))

    students.append({
        "id": student_id,
        "completed_courses": completed,
        "grades": grades,
        "GPA": gpa,
        "interests": interests
    })

# Convert to DataFrame for easy viewing
df = pd.DataFrame(students)

# Show the first 5 students
print(df.head(5))
