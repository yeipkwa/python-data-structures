class Vertex:

    def __init__(self, value):
        self.value = value
        self.edges = set()

    def add_edge(self, vertex):
        if vertex.value == self.value:
            print("You cannot add self as edge")
            return
        self.edges.add(vertex)


class Graph_Ds:
    def __init__(self, directed: bool):
        self.vertices = {}
        self.directed = directed

    def add_vertex(self, value):
        new_vertex = Vertex(value)
        self.vertices[value] = new_vertex

    def add_edge(self, value1, value2):
        if value1 not in self.vertices.keys() or value2 not in self.vertices.keys():
            print("Invalid Vertices")
            return
        if value1 == value2:
            print("Invalid Edge")
            return
        if self.directed:
            self.vertices[value1].add_edge(self.vertices[value2])
        else:
            self.vertices[value1].add_edge(self.vertices[value2])
            self.vertices[value2].add_edge(self.vertices[value1])

    def get_vertex(self, value):
        if value in self.vertices.keys():
            return self.vertices[value]
        return None

    def dfs(self, start, goal):
        '''
        :param start: node or vertex where search begins
        :param goal: node or vertex where search ends
        :return: path from start to goal if goal is found or None
        '''
        visited = []
        frontier = []
        parent_map = {}
        path = ""

        # Check if start is valid a node in graph
        if self.get_vertex(start):
            frontier.append(self.get_vertex(start))
        else:
            print("Invalid Start")
            return
        # continue search as long as the frontier is not empty
        while frontier:
            # immitating a stack by examining the node that was most recently added to the frontier for dfs.
            current_vertex = frontier[-1]
            # remove the last item from the frontier
            frontier = frontier[:-1]
            # print(current_vertex.value)
            # print([i.value for i in frontier])

            # checks if current node has been visited to avoid visiting twice (since children are probably already in frontier
            # or have been visited.
            if current_vertex.value in visited:
                # print(f"{current_vertex.value} has been visited. Skipping.")
                continue
            # If current vertex has been visited exit search and return path
            if current_vertex.value == goal:
                print("Path has been found")
                path += current_vertex.value
                parent = parent_map.get(current_vertex.value)
                while parent:
                    path += f" <- {parent}"
                    parent = parent_map.get(parent)
                return path
            # If goal has not been found add the current node to visited
            visited.append(current_vertex.value)
            # Append all the children or neighbours of the current node to the end of the frontier
            for edge in current_vertex.edges:
                frontier.append(edge)
                if edge.value in visited:
                    continue
                parent_map[edge.value] = current_vertex.value
            # print([i.value for i in frontier])

        print(f"There is no path between {start} and {goal}")
        return

    def bfs(self, start, goal):
        visited = []
        frontier = []
        path = ""
        parent_map = {}

        if self.get_vertex(start):
            frontier.append(self.get_vertex(start))
        else:
            print("Invalid Start")
            return
        while frontier:
            # print([i.value for i in frontier])
            current_node = frontier[0]
            frontier = frontier[1:]
            visited.append(current_node.value)
            if current_node.value == goal:
                print("Path has been found")
                # print(parent_map)
                path += f"{current_node.value}"
                parent = parent_map.get(current_node.value)
                while parent:
                    path += f" <- {parent}"
                    parent = parent_map.get(parent)
                return path

            for edge in current_node.edges:
                if edge.value in visited:
                    continue
                frontier.append(edge)
                parent_map[edge.value] = current_node.value
        print(f"There is no path between {start} and {goal}")
        return
