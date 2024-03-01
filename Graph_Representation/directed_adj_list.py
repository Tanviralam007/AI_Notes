# Adjacency List (Directed Graph)
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

        # Only append vertex2 to vertex1's list for directed edges
        adjacency_list[vertex1].append(vertex2)

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

def calculate_indegree(graph, vertex):
    indegree = 0
    for neighbors in graph.values():
        if vertex in neighbors:
            indegree = indegree + 1
    return indegree

def calculate_outdegree(graph, vertex):
    outdegree = len(graph[vertex])
    return outdegree

file_path = 'new_file.txt'
graph_list = read_graph_from_file(file_path)

print("Adjacency List:")
print_adjacency_list(graph_list)

selected_vertex = 0
# Calculate and print indegree and outdegree
indegree = calculate_indegree(graph_list, selected_vertex)
outdegree = calculate_outdegree(graph_list, selected_vertex)

print(f"Indegree of vertex {selected_vertex}: {indegree}")
print(f"Outdegree of vertex {selected_vertex}: {outdegree}")

"""
Expected Output:
Adjacency List:
0: [1]
1: [2, 3]
2: [3]
3: [0]
Indegree of vertex 0: 1
Outdegree of vertex 0: 1
"""