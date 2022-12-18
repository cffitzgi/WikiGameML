
class Article:
    def __init__(self, title, url, links, categories, heuristic=None):
        self.id = title #title of article
        self.connected_to = {}

        for i in links:
            self.add_neighbor(i)

        #self.parent = None
        self.url = url
        self.categories = categories
        self.h = heuristic
        self.g = 0

    def add_neighbor(self, neighbor, weight=0):
        # Add an entry to the connected_to dict with a given weight
        # TODO: Seems to be passing Article instead of key value. Can be fixed here or on line 93.
        if neighbor in self.connected_to.keys():
            self.connected_to[neighbor] = self.connected_to[neighbor] + 1
        else:
            self.connected_to[neighbor] = weight

    def set_h(self, h):
        # set article heuristics value
        self.h = h

    def __str__(self):
        # override __str__ for printing
        return(str(self.id) + ' connected to: ' + str([x.id for x in self.connected_to]))

    def get_connections(self):
        # return keys from connected_to dict
        return self.connected_to.keys()

    def get_id(self):
        # return article id's
        return self.id

    def get_h(self):
        # return article heuristics value
        return self.h

    def get_url(self):
        # return article URL
        return self.url

    def get_weight(self, neighbor):
        # return weights of edges connected to article
        return self.connected_to[neighbor]


class WikiNetwork:
    def __init__(self):
        # Dictionary of articles
        self.articles = {}
        # Article count
        self.num_vertices = 0

    def add_article(self, article: Article):
        a_id = article.get_id()
        if a_id in self.articles.keys():
            if self.articles[a_id].get_url() != "":
                return self.articles[a_id]
        else:
            self.num_vertices = self.num_vertices + 1

        new_vertex = article
        self.articles[article.id] = new_vertex
        return new_vertex

    def add_article_content(self, title, url, links, categories):
        if title in self.articles.keys():
            if self.articles[title].get_url() != "":
                return self.articles[title]
        else:
            # increment counter when adding article
            self.num_vertices = self.num_vertices + 1

        new_vertex = Article(title, url, links, categories)
        self.articles[new_vertex.id] = new_vertex
        return new_vertex

    def add_article_hollow(self, title):
        if title in self.articles.keys():
            return self.articles[title]

        # increment counter when adding article
        self.num_vertices = self.num_vertices + 1
        new_vertex = Article(title, "", {}, {})
        self.articles[title] = new_vertex
        return new_vertex

    def get_article(self, n):
        # check if article exists, return if True
        if n in self.articles.keys():
            return self.articles[n]
        else:
            return None

    def __contains__(self, n):
        # override __contains__ to list all vertices in WikiNetwork object
        return n in self.articles

    def add_edge(self, s, f, cost=0):
        # add edge to network; s = start node; e = end node
        if s not in self.articles.keys():
            self.add_article_hollow(s)
        if f not in self.articles.keys:
            self.add_article_hollow(f)
        self.articles[s].add_neighbor(self.articles[f], cost)

    def get_article_ids(self):
        # return keys of vertices in WikiNetwork
        return self.articles.keys()

    def get_articles(self):
        return self.articles.values()

    def get_urls(self):
        # return list of urls in WikiNetwork
        urls = []
        for vertex in self.articles.values():
            urls.append(vertex.url)
        return urls

    def __iter__(self):
        # override __iter__ to return iterable of vertices
        return iter(self.articles.values())
