# Adjacency List (Undirected Graph)
def read_first_line(file):
    # Read the first line for vertices and edges
    first_line = file.readline().split()
    return first_line[0], first_line[1]

def initialize_adjacency_list(num_vertices):
    # Initialize an empty dictionary with vertices as keys and empty lists as values
    adjacency_list = {}
    for vertex in range(num_vertices):
        adjacency_list[vertex] = []
    return adjacency_list

def read_edges(file, num_edges, adjacency_list):
    # Read the remaining lines for edge information
    for _ in range(num_edges):
        edge = file.readline().split()
        vertex1 = int(edge[0])
        vertex2 = int(edge[1])

        # Since the graph is undirected, append both vertices to each other's list
        adjacency_list[vertex1].append(vertex2)
        adjacency_list[vertex2].append(vertex1)

def read_graph_from_file(file_path):
    file = open(file_path, 'r')
    num_vertices_str, num_edges_str = read_first_line(file)
    num_vertices = int(num_vertices_str)
    num_edges = int(num_edges_str)
    
    adjacency_list = initialize_adjacency_list(num_vertices)
    read_edges(file, num_edges, adjacency_list)
    
    file.close()  # close the file
    return adjacency_list

def print_adjacency_list(adjacency_list):
    for vertex, neighbors in adjacency_list.items():
        print(f"{vertex}: {neighbors}")

# to find the degree of a node in an undirected graph
def degree_of_node(adjacency_list, node):
    # Find the degree of a node by counting its neighbours
    return len(adjacency_list[node])

file_path = 'file.txt' 
graph_list = read_graph_from_file(file_path)

print("Adjacency List:")
print_adjacency_list(graph_list)

node_to_check = 0  
degree = degree_of_node(graph_list, node_to_check)
print(f"Degree of node {node_to_check}: {degree}")

"""
Expected Output:

Adjacency List:
0: [1, 4, 2]
1: [0, 2, 3]
2: [1, 3, 0]
3: [2, 4, 1]
4: [3, 0]
Degree of node 0: 3

"""