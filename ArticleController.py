import ArticleModel


def AssembleGraph(vertices: dict):
    graph = ArticleModel.Graph()
    for key, value in vertices.items():
        graph.add_vertex(value)
        for link in value.connected_to:
            graph.add_edge(key, link)
    return graph

#class Controller:

