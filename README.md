# AI-Powered Academic Advisor — Astronomy Edition 🌌

This project is a response to a 48-hour research challenge to build an AI-powered academic advisor that can recommend personalized course paths to students based on interests, GPA, and prerequisite constraints. 

### 👩‍🚀 Theme: Astronomy Curriculum

---

## 📘 Overview

This system simulates a cohort of 100 astronomy students and provides smart course recommendations using graph modeling and heuristic planning.

- 🧠 Graph-based curriculum model (courses + prerequisites)
- 🪐 100 student profiles with GPA, grades, and interests
- 🤖 Heuristic advisor that suggests 3–5 next-term courses per student

---


## 📂 Folder Structure 
      ```
   ├── curriculum_graph.py # Builds and visualizes the astronomy course graph 
   ├── student_simulation.py # Generates 100 simulated student profiles
   ├── advisor_recommendation.py # Core AI logic for personalized course recommendations 
   ├── README.md # This file ```
   ├── report.pdf # 2-page project summary (explains design, logic, results) 
         ```



---

## 🧱 Technologies Used

- Python 3.x
- NetworkX (graph modeling)
- Matplotlib (visualization)
- Pandas (student data)
- Numpy (GPA calculations)


---

## 🔧 How to Run

1. Install dependencies:

```bash
pip install networkx matplotlib pandas numpy
```

2. Run each script in order:
```bash
python curriculum_graph.py
python student_simulation.py
python advisor_recommendation.py
```

---

## 💡 Key Concepts

- **Graph modeling**: Courses and prerequisites form a directed acyclic graph.
- **Heuristic planning**: Rules-based logic chooses next best courses based on:
  - Course eligibility (prereqs completed)
  - Interest matching
  - GPA improvement
  - Max 3–5 courses per term

---

## 🎓 Example Output

```json
{
  "student_id": 2,
  "interests": ["Cosmology"],
  "completed": ["A101", "A102", "A103", "A201", "A202"],
  "GPA": 3.4,
  "recommended_courses": ["A301", "A302", "A401"]
}

```
---

## ✨ Author

This project was developed by **Basmala Samir** in response to a research challenge.  
Special thanks to the team for the opportunity to explore intelligent academic systems for astronomy education.




