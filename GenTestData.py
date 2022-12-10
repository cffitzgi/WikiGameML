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
    all_links = []
    ## TODO: Store a list of all the links already collected to avoid going in circles/redundent path length.
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

        # For path length
        for i in range(self.path_length):
            # gets links and shuffles them to exclude redundant random picks.
            links = curr_article.get_page_links()
            random.shuffle(links)

            # Finds article that has not already been collected.
            next_article_url = links.pop(0)
            while next_article_url in self.all_links:
                next_article_url = links.pop(0)

            # Ensures article has specified minimum of outgoing links and has not been recorded.
            next_article = wr(WikiRead.full_link(next_article_url))
            while len(next_article.get_page_links()) < self.outgoing_links \
                or next_article_url in self.all_links:
                next_article_url = links.pop(0)
                next_article = wr(WikiRead.full_link(next_article_url))

            # Records links.
            self.all_links.extend(links)

            # Adds article to path and updates current article.
            self.path.append(curr_article)
            curr_article = next_article

        return self.path


def gen_raw_test_data(size, outgoing_links, path_length):
    paths = [[]]
    for i in range(size):
        paths.append(GenTestData(RANDOM, outgoing_links, path_length).gen())

    return paths


# Currently only uses categories as dataset. Article text could also be useful, but lets see how this goes.
# NOT CURRENTLY FUNCTIONAL! Need to change data to starting and goal article (need article model).
#       Answer key should be just the path. Need to set up ML algorithm to utilize WikiRead controller/API.
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