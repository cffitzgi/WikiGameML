import ArticleModel


def AssembleGraph(vertices: dict):
    graph = ArticleModel.Graph()
    for key, value in vertices.items():
        graph.add_vertex(value)
        #for link in iter(value.connected_to):
        #    graph.add_edge(key, value.connected_to[link])
    print("Graph assembled.")
    return graph

#class Controller:

