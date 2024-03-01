import heapq  # For priority queue

def ucs(graph, starting_node, goal_node):
    frontier = []  # Use a priority queue to prioritize paths by cost
    explored = []

    # Adding starting node with cost 0 to the priority queue
    heapq.heappush(frontier, (0, starting_node))

    while frontier:
        current_cost, current_node = heapq.heappop(frontier)
        explored.append(current_node)

        print("Visiting:", current_node, "(Cost:", current_cost, ")")

        if current_node == goal_node:
            return "Goal found!"

        for neighbor, neighbor_cost in graph[current_node].items():
            total_cost = current_cost + neighbor_cost
            if neighbor not in explored and (neighbor, total_cost) not in frontier:
                heapq.heappush(frontier, (total_cost, neighbor))

    return "Goal not found."

graph = {
    "A": {"B": 5, "C": 2},
    "B": {"D": 4, "E": 8},
    "C": {"F": 1},
    "D": {},
    "E": {"F": 2},
    "F": {}
}

starting_node = "A"
goal_node = "F"

result = ucs(graph, starting_node, goal_node)
print(result)