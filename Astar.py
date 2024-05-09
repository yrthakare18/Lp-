# Function implementing the A* algorithm to find the shortest path between two nodes in a graph
def aStarAlgo(start_node, stop_node):
    # Initialize the open set with the start node
    open_set = set(start_node)
    # Initialize the closed set
    closed_set = set()
    # Initialize the cost from the start node to each node in the graph
    g = {}
    # Initialize the parent nodes for each node in the graph
    parents = {}
    # Cost from start node to itself is 0
    g[start_node] = 0
    # Parent of the start node is itself
    parents[start_node] = start_node
    
    # Loop until open set is not empty
    while len(open_set) > 0:
        n = None
        # Find the node in the open set with the lowest cost
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        # If the current node is the goal node or there is no path from it
        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            # Iterate over the neighbors of the current node
            for (m, weight) in get_neighbors(n):
                # If the neighbor is not in the open or closed set
                if m not in open_set and m not in closed_set:
                    # Add it to the open set
                    open_set.add(m)
                    # Update its parent and cost from start node
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    # If the cost to reach the neighbor through the current node is lower than its current cost
                    if g[m] > g[n] + weight:
                        # Update the cost and parent of the neighbor
                        g[m] = g[n] + weight
                        parents[m] = n
                        # If the neighbor was in the closed set, move it back to the open set
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        # If there is no path found
        if n == None:
            print('Path does not exist!')
            return None
        # If the goal node is reached
        if n == stop_node:
            # Reconstruct the path from the goal node to the start node
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found: {}'.format(path))
            return path
        # Remove the current node from the open set and add it to the closed set
        open_set.remove(n)
        closed_set.add(n)
    # If the open set becomes empty and no path is found
    print('Path does not exist!')
    return None

# Function to get the neighbors of a node in the graph
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

# Heuristic function to estimate the cost from a node to the goal node
def heuristic(n):
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0
    }
    return H_dist[n]

# Graph representation
Graph_nodes = {
    'A': [('B', 6), ('C', 8),('D',7)],
    'B': [('A', 6), ('D', 8), ('E', 9)],
    'C': [('A', 8), ('D', 16), ('F', 12)],
    'D': [('A', 7), ('C', 16), ('E', 10),('G',21)],
    'E': [('B', 9), ('D', 10), ('H', 11)],
    'F': [('C', 12), ('G', 20)],
    'G': [('F', 20), ('H', 12)],
    'H': [('E', 11), ('G', 12)],
}

# Example usage
aStarAlgo('A', 'G')
