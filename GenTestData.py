import WikiScrape
from WikiScrape import WikiRead as wr
import random
import sklearn # in pip as "scikit-learn"
import IO

RANDOM = "https://en.wikipedia.org/wiki/Special:Random"


class TooFewOutgoingLinks(Exception):
    pass


# Generates a single testdata path of length n starting at start_link, with each article have at least k outgoing links
class GenTestData:
    path = []
    all_links = []

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
            links = curr_article.get_page_links().copy()
            random.shuffle(links)

            # Sheers article that have already been collected.
            for a in links:
                if a in self.all_links:
                    links.remove(a)

            # Ensures article has specified minimum of outgoing links and has not been recorded.
            next_article = wr(WikiRead.full_link(links.pop(0)))
            while len(next_article.get_page_links()) < self.outgoing_links:
                next_article_url = links.pop(0)
                next_article = wr(WikiRead.full_link(next_article_url))

            # Records links.
            links.append(curr_article.URL.split('/')[-1])
            self.all_links.extend(links)

            # Adds article to path and updates current article.
            self.path.append(curr_article)
            curr_article = next_article

        return self.path

'''
# Generates size number of testing data given parameters
def gen_raw_test_data(size, outgoing_links, path_length):
    paths = [[]]
    for i in range(size):
        paths.append(GenTestData(RANDOM, outgoing_links, path_length).gen())

    return paths
'''

# Generates size number of testing data with same starting article given parameters
def gen_raw_test_data(size, outgoing_links, path_length, starting_link=RANDOM):
    paths = [[]]
    for i in range(size):
        paths.append(GenTestData(starting_link, outgoing_links, path_length).gen())

    return paths


# Generates and writes to outfile n article paths for each combination of outgoing_links and path_distance values.
def new_testdata_file(out_file, n, outgoing_links, path_length):
    i = 1
    for p in path_length:
        for o in outgoing_links:
            print(f"Generating Dataset {i}...", end='')
            raw_data = gen_raw_test_data(n, o, p)
            print(f"done\nWriting Dataset {i}...", end='')
            if i == 1:  IO.write_test_data_csv(raw_data, out_file)
            else:       IO.append_test_data_csv(raw_data, out_file)
            print("done")
            i+=1

# Generates and writes to outfile n article paths for each combination of outgoing_links and path_distance values.
def add_testdata_file(out_file, n, outgoing_links, path_length):
    i = int(IO.get_last_id(out_file) / 50) + 1
    for p in path_length:
        for o in outgoing_links:
            print(f"Generating Dataset {i}...", end='')
            raw_data = gen_raw_test_data(n, o, p)
            print(f"done\nWriting Dataset {i}...", end='')
            IO.append_test_data_csv(raw_data, out_file)
            print("done")
            i+=1


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