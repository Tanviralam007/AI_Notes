def dfs(graph, starting_node, goal_node):
  # Use a list as a stack 
  frontier = [starting_node]
  explored = []  # Keep track of visited nodes

  while frontier:
    current_node = frontier.pop()  # Get the top node from the stack
    explored.append(current_node)  # Mark it as visited

    print("Visiting:", current_node)  # Show where we are

    # If we found the goal, done!
    if current_node == goal_node:
      return "Goal found!"

    # Explore neighbors in a "depth-first" way
    for neighbor in graph[current_node]:
      if neighbor not in explored and neighbor not in frontier:
        frontier.append(neighbor)  # Add them to the top of the stack

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

result = dfs(graph, starting_node, goal_node)
print(result)
