def heuristic(node, goal_node):
  """Estimates the distance from a node to the goal node."""
  # Replace with your actual heuristic function
  heuristic_values = {
      "A": 5, "B": 3, "C": 2, "D": 7, "E": 1, "F": 0,
      "G": 4, "H": 8, "I": 6, "J": 9, "K": 10, "L": 11, "M": 12
  }
  return heuristic_values[node]

def calculate_f_value(g_value, h_value):
  """Calculates the total A* score (f(n)) for a node."""
  return g_value + h_value

def astar(graph, starting_node, goal_node):
  """Performs A* search on a graph to find the goal node."""
  open_list = [starting_node]
  closed_list = {}
  g_value = {starting_node: 0}  # Cost from starting node to each explored node

  while open_list:
    current_node = min(open_list, key=lambda node: calculate_f_value(g_value.get(node, 0), heuristic(node, goal_node)))
    open_list.remove(current_node)

    if current_node == goal_node:
      return "Goal found!"

    closed_list[current_node] = g_value[current_node]

    for neighbor in graph[current_node]:
      if neighbor in closed_list:
        continue

      tentative_g_value = g_value[current_node] + 1

      if neighbor not in open_list or tentative_g_value < g_value.get(neighbor, float('inf')):
        open_list.append(neighbor)
        g_value[neighbor] = tentative_g_value

  return "Goal not found."

graph = {
  "A": ["B", "C"],
  "B": ["D", "E"],
  "C": ["F", "G"],
  "D": ["H", "I"],
  "E": ["J"],
  "F": [],
  "G": ["K"],
  "H": ["L"],
  "I": ["M"],
  "J": [],
  "K": [],
  "L": [],
  "M": []
}

starting_node = "A"
goal_node = "F"

result = astar(graph, starting_node, goal_node)
print(result)
