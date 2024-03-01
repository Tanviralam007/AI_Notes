# Reversed Graph Showed 2

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

# Print reversed edges
print("Reversed Edges:")
for vertex, neighbors in reversed_graph.items():
    for neighbor in neighbors:
        print(f"{vertex}--{neighbor}")
"""
Expected Output:
Reversed Edges:
5 -- 4
1 -- 0
2 -- 1
3 -- 1
3 -- 2
0 -- 3
"""