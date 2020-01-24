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
        self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if(v1 in self.vertices and v2 in self.vertices):
            return self.vertices[v1].add(v2)
        raise IndexError("Invalid vertices")
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if(vertex_id in self.vertices):
            return self.vertices[vertex_id]
        raise IndexError("Invalid vertex")
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue/stack as appropriate
        queue = Queue()
        # Put the starting point in that
        queue.enqueue(starting_vertex)
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while queue.size() > 0:
            #    Pop the first item
            vertex = queue.dequeue()
        #    If not visited
            if vertex not in visited:
                #       DO THE THING!
                print(vertex)
                visited.add(vertex)
        #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                    #           Add that edge to the queue/stack
                    queue.enqueue(next_vert)
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a queue/stack as appropriate
        stack = Stack()
        # Put the starting point in that
        stack.push(starting_vertex)
        # Make a set to keep track of where we've been
        visited = set()
        answer = []
        i = 0
        # While there is stuff in the queue/stack
        while stack.size() > 0:
            #    Pop the first item
            vertex = stack.pop()
        #    If not visited
            if vertex not in visited:
                #       DO THE THING!
                visited.add(vertex)
                
                answer.append((vertex, i))
        #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                    #           Add that edge to the queue/stack
                    stack.push(next_vert)
                    i += 1
        return answer
    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                self.dft_recursive(child_vert, visited)
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue/stack as appropriate
        queue = Queue()
        # Put the starting point in that
        # Enstack a list to use as our path
        queue.enqueue([starting_vertex])
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while queue.size() > 0:
            #    Pop the first item
            path = queue.dequeue()
            vertex = path[-1]
        #    If not visited
            if vertex not in visited:
                if vertex == destination_vertex:
                    # Do the thing!
                    return path
                visited.add(vertex)
        #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                    # Copy path to avoid pass by reference bug
                    # Make a copy of path rather than reference
                    new_path = list(path)
                    new_path.append(next_vert)
                    queue.enqueue(new_path)
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a queue/stack as appropriate
        stack = Stack()
        # Put the starting point in that
        # Enstack a list to use as our path
        stack.push([starting_vertex])
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while stack.size() > 0:
            #    Pop the first item
            path = stack.pop()
            vertex = path[-1]
        #    If not visited
            if vertex not in visited:
                if vertex == destination_vertex:
                    # Do the thing!
                    return path
                visited.add(vertex)
        #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                    # Copy path to avoid pass by reference bug
                    # Make a copy of path rather than reference
                    new_path = list(path)
                    new_path.append(next_vert)
                    stack.push(new_path)
    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == destination_vertex:
            return path
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                new_path = self.dfs_recursive(
                    child_vert, destination_vertex, visited, path)
                if new_path:
                    return new_path
        return None