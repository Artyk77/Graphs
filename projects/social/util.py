class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edges(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Can not create edge based on given vertices")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        qq = Queue()
        visited = set()

        qq.enqueue(starting_vertex)

        while qq.size() > 0:
            vertex = qq.dequeue()

            if vertex not in visited:
                visited.add(vertex)
                print(vertex)

                for next_vert in self.vertices[vertex]:
                    qq.enqueue(next_vert)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()

        stack.push(starting_vertex)

        while stack.size() > 0:
            vertex = stack.pop()

            if vertex not in visited:
                visited.add(vertex)
                print(vertex)

                for next_vert in self.vertices[vertex]:
                    stack.push(next_vert)


    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if starting_vertex in visited:
            return

        visited.add(starting_vertex)
        if len(self.vertices[starting_vertex]) == 0:
            return

        print(starting_vertex)

        for next_vert in self.vertices[starting_vertex]:
            self.dft_recursive(next_vert)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        qq = Queue()
        visited = set()

        qq.enqueue([starting_vertex])

        while qq.size() > 0:
            path = qq.dequeue()
            vertex = path[-1]

            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                for next_vert in self.vertices[vertex]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited = set()
        path=[]

        stack.push(starting_vertex)

        while stack.size() > 0:
            vertex = stack.pop()

            if vertex not in visited:
                visited.add(vertex)
                path.append(vertex)
                if vertex == destination_vertex:
                    return path

                for next_vert in self.vertices[vertex]:
                    stack.push(next_vert)
