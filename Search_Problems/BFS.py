def bfs(graph, starting_node, goal_node):
    # Use a list as a queue 
    frontier = []
    explored = []  # Keep track of visited nodes

    # Start at the starting node
    frontier.append(starting_node)

    while frontier:  # Keep going until the frontier queue is empty
        current_node = frontier.pop(0)  # Get the first one in line
        explored.append(current_node)  # Mark it as visited

        print("Visiting:", current_node)

        # If we found the goal, done!
        if current_node == goal_node:
            return "Goal found!"

        # Explore neighbors in a "breadth-first" way
        for neighbor in graph[current_node]:
            if neighbor not in explored and neighbor not in frontier:
                frontier.append(neighbor)  # Add them to the back of the line

    return "Goal not found."

# Sample graph (like a map of connected cities)
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

starting_node = "E"
goal_node = "F"

result = bfs(graph, starting_node, goal_node)
print(result)