import ArticleModel


def AssembleGraph(vertices: dict):
    graph = ArticleModel.Graph()
    for key, value in vertices.items():
        graph.add_vertex(value)
        #for link in iter(value.connected_to):
        #    graph.add_edge(key, value.connected_to[link])
    print("Graph assembled.")
    return graph

def AssembleRootedGraph(vertices: dict, root_node: ArticleModel.Vertex, graph: ArticleModel.Graph):
    for child in root_node.connected_to:
        if not child in graph.vertices_list:
            root_node.connected_to[child] = vertices[child]
    for child in (graph.vertices_list[root_node.id]).connected_to:
        AssembleRootedGraph(vertices, child, graph)
    return graph

def ApplyHeuristic(heuristic):
    print("Unfinished.")

#class Controller:

