def gbfs(graph, starting_node, goal_node, heuristic_values):
  # Use a priority queue (like a line with VIP access)
  frontier = [(heuristic_values[starting_node], starting_node)]
  explored = []  # Keep track of visited nodes

  while frontier:
    # Get the node with the lowest heuristic value (appears closest to goal)
    current_node = frontier.pop(0)[1]
    explored.append(current_node)  # Mark it as visited

    print("Visiting:", current_node)  # Show where we are

    # If we found the goal, done!
    if current_node == goal_node:
      return "Goal found!"

    # Explore neighbors in a greedy way
    for neighbor in graph[current_node]:
      if neighbor not in explored:
        # Add neighbor with its heuristic value to the priority queue
        frontier.append((heuristic_values[neighbor], neighbor))
      # Sort the queue by heuristic value (lower is better)
      frontier.sort()

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
goal_node = "K"

# Sample heuristic values
heuristic_values = {
  "A": 5,
  "B": 3,
  "C": 2,
  "D": 4,
  "E": 7,
  "F": 1,
  "G": 6,
  "H": 8,
  "I": 9,
  "J": 10,
  "K": 0,  # Assuming goal is here
  "L": 11,
  "M": 12
}

result = gbfs(graph, starting_node, goal_node, heuristic_values)
print(result)
