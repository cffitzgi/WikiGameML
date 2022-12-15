import ArticleModel

class Controller:
    def AssembleGraph(self, vertices):
        graph = ArticleModel.Graph()
        for vertex in vertices:
            graph.add_vertex(vertex)
            for link in vertex.connected_to:
                graph.add_edge(vertex.id, link)
        return graph
