"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # Create the new key with the vertex ID, and set the value to an empty set (meaning no edges yet)
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Find vertex V1 in our vertices, add V2 to the set of edges
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a var for the Queue class
        queue = Queue()

        # Call the enqueue method from the Queue class
        # and pass in the starting_vertex in it
        queue.enqueue(starting_vertex)

        # Create a set to store the visited vertices
        visited_vertices = set()

        # Do a while loop through the length of the queue from zero and up
        while queue.size() > 0:
            # Create a var for the current vertex and use the dequeue method
            # from the Queue class
            current_vertex = queue.dequeue()
            # See if the current vertex is not in visited vertices
            # print and then add it to the visited vertices set
            if current_vertex not in visited_vertices:
                print(current_vertex)
                visited_vertices.add(current_vertex)

                # Add all neighbors to the queue
                for neighbor in self.get_neighbors(current_vertex):
                    queue.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a var for the Stack class
        stack = Stack()

        # Call the push method from the Stack class
        # and pass in the starting_vertex in it
        stack.push(starting_vertex)

        # Create a set to store the visited vertices
        visited_vertices = set()

        # Do a while loop through the length of the stack from zero and up
        while stack.size() > 0:
            # Create a var for the current vertex and use the pop method
            # from the Stack class
            current_vertex = stack.pop()
            # See if the current vertex is not in visited vertices
            # print and then add it to the visited vertices set
            if current_vertex not in visited_vertices:
                print(current_vertex)
                visited_vertices.add(current_vertex)

                # Add all neighbors to the queue
                for neighbor in self.get_neighbors(current_vertex):
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited_ver=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Create a var called current_ver for the starting_vertex
        # and then print it
        current_ver = starting_vertex
        print(current_ver)

        # See if the vertex has been visited
        if visited_ver is None:
            # this is a set to store visited vertices
            visited_ver = set()
        # Add the current vertex to the visited ver
        visited_ver.add(current_ver)

        # Loop through the neighbors of the current vertex
        # and see if it's not in the visited set
        # then called the function itself and pass on the neighbor and the visited ver
        for neighbor in self.get_neighbors(current_ver):
            if neighbor not in visited_ver:
                self.dft_recursive(neighbor, visited_ver)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a var for the Queue class
        queue = Queue()

        # Call the enqueue method from the Queue class
        # and pass in the starting_vertex in it as an array
        queue.enqueue([starting_vertex])

        # Create a set to store the visited vertices
        visited_vertices = set()

        # Do a while loop through the length of the queue from zero and up
        while queue.size() > 0:
            # Create a var for the current vertex path and use the dequeue method
            # from the Queue class
            current_ver_path = queue.dequeue()
            # Set the current vertex to the last element of the path
            # and see if it's not in the visited vertices and if it's the destination
            # then add it to the visited vertices and stop and return
            if current_ver_path[-1] not in visited_vertices and current_ver_path[-1] == destination_vertex:
                visited_vertices.add(current_ver_path[-1])
                return current_ver_path

            # Add all neighbors to the queue
            for neighbor in self.get_neighbors(current_ver_path[-1]):
                new_ver_path = [*current_ver_path, neighbor]
                queue.enqueue(new_ver_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a var for the Stack class
        stack = Stack()

        # Call the push method from the Stack class
        # and pass in the starting_vertex in it as an array
        stack.push([starting_vertex])

        # Create a set to store the visited vertices
        visited_vertices = set()

        # Do a while loop through the length of the stack from zero and up
        while stack.size() > 0:
            # Create a var for the current vertex path and use the pop method
            # from the Stack class
            current_ver_path = stack.pop()
            # Set the current vertex to the last element of the path
            # and see if it's not in the visited vertices and if it's the destination
            # then add it to the visited vertices and stop and return
            if current_ver_path[-1] not in visited_vertices and current_ver_path[-1] == destination_vertex:
                visited_vertices.add(current_ver_path[-1])
                return current_ver_path

            # Add all neighbors to the queue
            for neighbor in self.get_neighbors(current_ver_path[-1]):
                new_ver_path = [*current_ver_path, neighbor]
                stack.push(new_ver_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited_ver=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # See if the vertex has been visited
        if visited_ver is None:
            # this is a set to store visited vertices
            visited_ver = set()

        # See if the  path exists
        if path is None:
            # this is an array to store the paths
            path = []

         # Add the starting vertex to the visited vertex set
        visited_ver.add(starting_vertex)

        # Create a path var and add it with the starting vertex
        path = path + [starting_vertex]

        # See if we are at the destination
        if starting_vertex == destination_vertex:
            # if it is then return the path
            return path

        # Loop through the neighbors of the current vertex
        # and see if it's not in the visited set
        # then called the function itself and pass on the neighbor,
        # the distination vertex, the visited ver and the path
        # and set it to be the new path
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited_ver:
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited_ver, path)
                # if items are within the new_path, return it
                if new_path is not None:
                    return new_path



if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
