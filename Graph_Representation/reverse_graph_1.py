# Reversed Graph Showed 1

# Read the file
file_path = "new_file.txt"

with open(file_path, 'r') as file:
    lines = file.readlines()

# Create a dictionary to represent the graph
graph = {}

# Add edges to the graph and reverse the direction
for line in lines:
    vertex1, vertex2 = line.strip().split()

    # Add edges to the graph
    if vertex1 not in graph:
        graph[vertex1] = []
    graph[vertex1].append(vertex2)

# Reverse the direction of each edge
reversed_graph = {}

for vertex, neighbors in graph.items():
    for neighbor in neighbors:
        if neighbor not in reversed_graph:
            reversed_graph[neighbor] = []
        reversed_graph[neighbor].append(vertex)

# create a new file with reversed edges
new_file_path = "reversed_graph.txt"

with open(new_file_path, 'w') as new_file:
    for vertex, neighbors in reversed_graph.items():
        for neighbor in neighbors:
            new_file.write(f"{vertex} {neighbor}\n")

print(f"Graph direction reversed and saved to {new_file_path}")
