# Adjacency Matrix (Directed Graph)
def read_first_line(file):
    # Read the first line for vertices and edges
    first_line = file.readline().split()
    return first_line[0], first_line[1]

def initialize_adjacency_matrix(num_vertices):
    # Initialize an empty matrix with all zeros
    adjacency_matrix = []
    for _ in range(num_vertices):
        row = [0] * num_vertices
        adjacency_matrix.append(row)
    return adjacency_matrix

def read_edges(file, num_edges, adjacency_matrix):
    # Read the remaining lines for edge information
    for i in range(num_edges):
        edge = file.readline().split()
        vertex1 = int(edge[0])
        vertex2 = int(edge[1])

        # Set the entry to 1 for a directed edge
        adjacency_matrix[vertex1][vertex2] = 1

def read_graph_from_file(file_path):
    file = open(file_path, 'r')
    num_vertices_str, num_edges_str = read_first_line(file)
    num_vertices = int(num_vertices_str)
    num_edges = int(num_edges_str)
    
    adjacency_matrix = initialize_adjacency_matrix(num_vertices)
    read_edges(file, num_edges, adjacency_matrix)
    
    file.close()  # close the file
    return adjacency_matrix

def print_adjacency_matrix(adjacency_matrix):
    for row in adjacency_matrix:
        for element in row:
            print(element, end=" ")
        print()

# Calculate the indegree of a node in a directed graph
def calculate_indegree(adjacency_matrix, node):
    indegree = 0
    for row in adjacency_matrix:
        indegree = indegree + row[node]
    return indegree
    
# Calculate the outdegree of a node in a directed graph
def calculate_outdegree(adjacency_matrix, node):
    outdegree = sum(adjacency_matrix[node])
    return outdegree

file_path = 'new_file.txt' 
graph_matrix = read_graph_from_file(file_path)

print("Adjacency Matrix:")
print_adjacency_matrix(graph_matrix)

node_to_check = 2
indegree = calculate_indegree(graph_matrix, node_to_check)
outdegree = calculate_outdegree(graph_matrix, node_to_check)

print(f"Indegree of Node {node_to_check}: {indegree}")
print(f"Outdegree of Node {node_to_check}: {outdegree}")

"""
Expected Ouput:
Adjacency Matrix:
0 1 0 0 
0 0 1 1 
0 0 0 1 
1 0 0 0 
Indegree of Node 2: 1
Outdegree of Node 2: 1
"""