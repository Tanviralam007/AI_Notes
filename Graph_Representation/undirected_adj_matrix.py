# Adjacency Matrix (undirected graph)
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

        # Since the graph is undirected, set both entries to 1
        adjacency_matrix[vertex1][vertex2] = 1
        adjacency_matrix[vertex2][vertex1] = 1

def read_graph_from_file(file_path):
    file = open(file_path, 'r')
    num_vertices_str, num_edges_str = read_first_line(file)
    num_vertices = int(num_vertices_str)
    num_edges = int(num_edges_str)
    
    adjacency_list = initialize_adjacency_matrix(num_vertices)
    read_edges(file, num_edges, adjacency_list)
    
    file.close()  # close the file
    return adjacency_list

def print_adjacency_matrix(adjacency_matrix):
    for row in adjacency_matrix:
        for element in row:
            print(element, end=" ")
        print()

# to find the degree of a node in an undirected graph
def find_node_degree(adjacency_matrix, node):
    # Sum the values in the row corresponding to the node
    return sum(adjacency_matrix[node])

file_path = 'file.txt' 
graph_matrix = read_graph_from_file(file_path)

print("Adjacency Matrix:")
print_adjacency_matrix(graph_matrix)

node_to_check = 0
degree = find_node_degree(graph_matrix, node_to_check)
print(f"Degree of Node {node_to_check}: {degree}")

"""
Expected Output:

Adjacency Matrix:
0 1 1 0 1
1 0 1 1 0
1 1 0 1 0
0 1 1 0 1
1 0 0 1 0
Degree of Node 0: 3
"""