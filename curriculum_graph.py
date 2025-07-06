import networkx as nx
import matplotlib.pyplot as plt

# Initialize a graph
G = nx.DiGraph()

# Astronomy Curriculum (course prerequisites)
courses = {
    "A101": [],  # Intro to Astronomy
    "A102": [],  # General Physics I
    "A103": [],  # Calculus I
    "A201": ["A101"],  # Observational Astronomy
    "A202": ["A102"],  # General Physics II
    "A203": ["A103"],  # Calculus II
    "A301": ["A201", "A202"],  # Stellar Astrophysics
    "A302": ["A201", "A202"],  # Galactic Astronomy
    "A303": ["A201", "A202", "A203"],  # Planetary Science
    "A401": ["A301", "A302"],  # Cosmology
    "A402": ["A303"]  # Astrobiology
}

# Add edges (prerequisite relationships)
for course, prereqs in courses.items():
    for prereq in prereqs:
        G.add_edge(prereq, course)

# Draw the graph
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="plum", font_size=10, font_weight="bold", arrowsize=20)
plt.title("Astronomy Curriculum Graph", fontsize=14)
plt.show()
