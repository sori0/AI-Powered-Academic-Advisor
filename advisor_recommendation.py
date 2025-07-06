import json
import pandas as pd
import networkx as nx

# Load the student data 
from student_simulation import students

# Build curriculum graph again
G = nx.DiGraph()
courses = {
    "A101": [],
    "A102": [],
    "A103": [],
    "A201": ["A101"],
    "A202": ["A102"],
    "A203": ["A103"],
    "A301": ["A201", "A202"],
    "A302": ["A201", "A202"],
    "A303": ["A201", "A202", "A203"],
    "A401": ["A301", "A302"],
    "A402": ["A303"]
}
for course, prereqs in courses.items():
    for prereq in prereqs:
        G.add_edge(prereq, course)

# Interest mapping: match keywords to course codes
interest_to_courses = {
    "Stellar Astrophysics": ["A301", "A401"],
    "Galactic Astronomy": ["A302", "A401"],
    "Planetary Science": ["A303", "A402"],
    "Cosmology": ["A401"],
    "Astrobiology": ["A402"],
    "Observational Techniques": ["A201"]
}

def get_eligible_courses(student_courses):
    eligible = []
    for course in courses.keys():
        if course in student_courses:
            continue  # already completed
        prereqs = courses[course]
        if all(p in student_courses for p in prereqs):
            eligible.append(course)
    return eligible

# Generate recommendations for each student
recommendations = []

for student in students:
    completed = student["completed_courses"]
    interests = student["interests"]

    eligible_courses = get_eligible_courses(completed)

    # Prioritize courses that match interests
    preferred = []
    for interest in interests:
        if interest in interest_to_courses:
            for c in interest_to_courses[interest]:
                if c in eligible_courses and c not in preferred:
                    preferred.append(c)

    final_recommend = preferred.copy()
    for c in eligible_courses:
        if c not in final_recommend:
            final_recommend.append(c)
        if len(final_recommend) >= 5:
            break

    recommendations.append({
        "student_id": student["id"],
        "interests": interests,
        "completed": completed,
        "GPA": student["GPA"],
        "recommended_courses": final_recommend
    })

# View 3 examples
for r in recommendations[:3]:
    print(json.dumps(r, indent=2))
