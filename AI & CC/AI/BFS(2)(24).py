from collections import deque  # Import deque for efficient queue operations

# Function to add an edge to the graph (undirected)
def add_edge(graph, u, v):
    # For undirected graph, add both u->v and v->u
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

# Recursive BFS function
def bfs_recursive(queue, visited, graph):
    if not queue:
        return  # Base case: stop recursion if queue is empty

    node = queue.popleft()  # Dequeue the front node

    if node not in visited:
        print(node, end=" ")  # Process the node (print it)
        visited.add(node)     # Mark the node as visited

        # Enqueue all unvisited neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

    # Recursive call to continue BFS traversal
    bfs_recursive(queue, visited, graph)

# Main function to handle input and start BFS
def main():
    graph = {}  # Dictionary to store adjacency list of graph
    edges = int(input("How many edges? "))  # Get number of edges

    # Add each edge to the graph
    for _ in range(edges):
        u, v = input("Enter edge (e.g. A B): ").split()
        add_edge(graph, u, v)

    start = input("Start BFS from node: ")  # Starting node for BFS

    print("Recursive BFS Traversal:")
    # Start BFS with initial node in queue and empty visited set
    bfs_recursive(deque([start]), set(), graph)

# Entry point of the program
if __name__ == "__main__":
    main()
