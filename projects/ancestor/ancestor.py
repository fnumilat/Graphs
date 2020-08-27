## Understanding Phase:

# Input date: a graph of relationships between parents 
# and children over multiple generations.

# Data format: a list of (parent, child) pairs.
# * Each individual is assigned a unique integer id.

# Output: to return an individual's earliest known ancestor - 
# the one at the farthest distance from the input individual.
# *If there is more than one ancestor tied for "earliest", 
# return the one with the lowest numeric id.
# * If the input individual has no parents, the function should return -1.

## Planning and Execution Phase:

# Using the Queue method to accomplish this task
from util import Queue
# Using the Graph class to create the graph for this task
from graph import Graph


def earliest_ancestor(ancestors, starting_node):

    # Call the Graph method and create a var for it
    graph = Graph()
    
    # Loop through the ancestors
    # and create vertexes and edges
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        graph.add_edge(pair[1], pair[0])

    
    # Call the Queue method and create a var for it
    queue = Queue()

    # Add the starting node to the queue
    queue.enqueue([starting_node])

    # Create a set to store the visited vertices
    visited = set()

    # Set the earliest ancestor to -1 if the input individual has no parents
    earliest_ancestor = -1

    # While the queue's lenght is not zero
    while queue.size() > 0:
        # Create a var called path to dequeue
        path = queue.dequeue()
        # Create a var called vertex to get the last 
        # node in the path
        vertex = path[-1]

        # See if the vertex has been visited
        # then mark it as visited
        if vertex not in visited:
            visited.add(vertex)

            # See if the vertex is less than the parent then
            # set the parent as the vertex
            if ((vertex < earliest_ancestor) or (len(path)> 1)):
                earliest_ancestor = vertex

            # Check for the neighbors of the vertex
            # copy the path
            # add the neighbor to the path
            # and add the path to the queue
            for neighbor in graph.get_neighbors(vertex):
                new_path = path.copy()
                new_path.append(neighbor)
                queue.enqueue(new_path)

    return earliest_ancestor

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

    # 
    #    10
    #  /
    # 1   2   4  11
    #  \ /   / \ /
    #   3   5   8
    #    \ / \   \
    #     6   7   9
    # 

print(f'The earliest ancestor of 1>> {earliest_ancestor(test_ancestors, 1)}')
print(f'The earliest ancestor of 2>> {earliest_ancestor(test_ancestors, 2)}')
print(f'The earliest ancestor of 3>> {earliest_ancestor(test_ancestors, 3)}')
print(f'The earliest ancestor of 4>> {earliest_ancestor(test_ancestors, 4)}')
print(f'The earliest ancestor of 5>> {earliest_ancestor(test_ancestors, 5)}')
print(f'The earliest ancestor of 6>> {earliest_ancestor(test_ancestors, 6)}')
print(f'The earliest ancestor of 7>> {earliest_ancestor(test_ancestors, 7)}')
print(f'The earliest ancestor of 8>> {earliest_ancestor(test_ancestors, 8)}')
print(f'The earliest ancestor of 9>> {earliest_ancestor(test_ancestors, 9)}')
print(f'The earliest ancestor of 10>> {earliest_ancestor(test_ancestors, 10)}')
print(f'The earliest ancestor of 11>> {earliest_ancestor(test_ancestors, 11)}')




    