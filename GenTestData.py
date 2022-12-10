import WikiRead
from WikiRead import WikiRead as wr
import random
import sklearn # in pip as "scikit-learn"

RANDOM = "https://en.wikipedia.org/wiki/Special:Random"

class TooFewOutgoingLinks(Exception):
    pass

# Generates a single test-data path of length n starting from start_link, with each article have at least k outgoing links
class GenTestData:
    path = []

    def __init__(self, start_link, outgoing_links, path_length):
        self.outgoing_links = outgoing_links
        self.path_length = path_length
        self.article = wr(start_link)
        if len(self.article.get_page_links()) < outgoing_links:
            if start_link == RANDOM:
                new = GenTestData(RANDOM,outgoing_links,path_length)
                self.outgoing_links = new.outgoing_links
                self.path_length = new.path_length
                self.article = new.article
            else:
                raise TooFewOutgoingLinks()

    # Generates test-data path given initialized start_link. WARNING: Each run overwrites path.
    def gen(self):
        self.path = []
        curr_article = self.article
        for i in range(self.path_length):
            links = curr_article.get_page_links()

            next_article_url = random.choice(links)
            next_article = wr(WikiRead.full_link(next_article_url))
            while len(next_article.get_page_links()) < self.outgoing_links:
                next_article_url = random.choice(links)
                next_article = wr(WikiRead.full_link(next_article_url))

            self.path.append(curr_article)
            curr_article = next_article

        return self.path


def gen_raw_test_data(size, outgoing_links, path_length):
    paths = [[]]
    for i in range(size):
        paths.append(GenTestData(RANDOM, outgoing_links, path_length))

    return paths


# Currently only uses categories as dataset. Article text could also be useful, but lets see how this goes.
def preprocess_dataset(dataset, t_size):
    data = [[[]]]
    answers = [[]]
    for p in dataset:
        data_categories = [[]]
        path = []
        for a in p:
            path.append(a.URL)
            data_categories.append(a.categories)
        data.append(data_categories)
        answers.append(path)

    return sklearn.model_selection.train_test_split(data, answers, test_size=t_size)