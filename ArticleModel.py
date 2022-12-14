class Vertex:
    def __init__(self, title, url, links, heuristic = 0):
        self.id = title #title of article
        self.connected_to = links #links
        self.parent = None
        self.url = url
        self.h = heuristic
        self.g = 0

    def add_neighbor(self, neighbor, weight=0):
        # Add an entry to the connected_to dict with a given
        # weight
        self.connected_to[neighbor] = weight

    def set_h(self, h):
        # set vertex heuristics value
        self.h = h

    def __str__(self):
        # override __str__ for printing
        return(str(self.id) + ' connected to: ' + str([x.id for x in self.connected_to]))

    def get_connections(self):
        # return keys from connected_to dict
        return self.connected_to.keys()

    def get_id(self):
        # return vertex id's
        return self.id

    def get_h(self):
        # return vertex heuristics value
        return self.h

    def get_weight(self, neighbor):
        # return weights of edges connected to vertex
        return self.connected_to[neighbor]

class Graph:
    def __init__(self):
        # dictionary of vertices
        self.vertices_list = {}
        # vertex count
        self.num_vertices = 0

    def add_vertex(self, vertex):
        # increment counter when adding vertex
        self.num_vertices = self.num_vertices + 1
        new_vertex = vertex
        self.vertices_list[vertex.id] = new_vertex
        return new_vertex
    
    def add_vertex2(self, title, url, links):
        #increment counter when adding vertex
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(title, url, links)
        self.vertices_list[new_vertex.id] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        # check if vertex exists, return if True
        if n in self.vertices_list:
            return self.vertices_list[n]
        else:
            return None

    def __contains__(self, n):
        # override __contains__ to list all vertices in Graph object
        return n in self.vertices_list

    def add_edge(self, s, f, cost=0):
        # add edge to graph; s = start node; e = end node
        if s not in self.vertices_list:
            self.add_vertex(s)
        if f not in self.vertices_list:
            self.add_vertex(f)
        self.vertices_list[s].add_neighbor(self.vertices_list[f], cost)

    def get_vertices(self):
        # return keys of vertices in Graph
        return self.vertices_list.keys()

    def __iter__(self):
        # override __iter__ to return iterable of vertices
        return iter(self.vertices_list.values())