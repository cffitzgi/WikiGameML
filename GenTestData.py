import WikiRead
from WikiRead import WikiRead as wr
import random

RANDOM = "https://en.wikipedia.org/wiki/Special:Random"

class TooFewOutgoingLinks(Exception):
    pass

class GenTestData:
    path = []

    def __init__(self, start_link, k, n):
        self.k = k
        self.n = n
        self.article = wr(start_link)
        if len(self.article.get_page_links()) < k:
            if start_link == RANDOM:
                self = GenTestData(RANDOM, k, n)
            else:
                raise TooFewOutgoingLinks()

    def gen(self):
        self.path = []
        curr_article = self.article
        for i in range(1,self.n):
            links = curr_article.get_page_links()

            next_article_url = random.choice(links)
            next_article = wr(next_article_url)
            while len(next_article.get_page_links()) < self.k:
                next_article_url = random.choice(links)
                next_article = wr(next_article_url)

            self.path.append(curr_article)
            curr_article = next_article

        return self.path
