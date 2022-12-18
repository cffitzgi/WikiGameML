from Network import ArticleModel
from Network.ArticleModel import Article
from Network.ArticleModel import WikiNetwork
import jsonpickle


def ReadNetwork(path):
    print("Opening Network...", end="")
    with open(path, 'r', encoding='utf-16') as file:
        j = file.read()
        print("done.")
        return jsonpickle.decode(j)


def WriteNetwork(path, network):
    print("Saving Network...", end="")
    n = jsonpickle.encode(network)
    with open(path, 'w', encoding='utf-16') as file:
        file.write(n)
    print("done.")

def AssembleNetwork(vertices: dict):
    graph = ArticleModel.WikiNetwork()
    for key, value in vertices.items():
        graph.add_article(value)
        #for link in iter(value.connected_to):
        #    network.add_edge(key, value.connected_to[link])
    print("WikiNetwork assembled.")
    return graph


def AssembleRootedNetwork(vertices: dict, root_node: Article, network: WikiNetwork):
    for child in root_node.connected_to:
        if not child in network.articles:
            root_node.connected_to[child] = vertices[child]
    for child in (network.articles[root_node.id]).connected_to:
        AssembleRootedNetwork(vertices, child, network)
    return network


def ApplyHeuristic(heuristic):
    print("Unfinished.")

#class Controller:

