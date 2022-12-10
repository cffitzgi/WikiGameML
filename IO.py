from WikiRead import WikiRead as wr
import csv

dataset_count = 0

# Writes dataset to path.
def write_test_data_csv(dataset: [[wr]], path):
    with open(path, 'w', newline='', encoding='utf-16') as file:
        # Header stuff, and starts writer.
        fieldnames = ['d_id', 'title', 'url', 'links', 'categories']
        w = csv.DictWriter(file, fieldnames=fieldnames)
        w.writeheader()

        # For each path...
        d_id = 0            # Distinguishes each path.
        for d in dataset:
            # Write each article...
            for a in d:
                safe_write(w, d_id, a.title, a.URL, a.links, a.categories)
            d_id += 1

def safe_write(writer, d_id, title, URL, links, categories):
    try:
        writer.writerow({'d_id': d_id, 'title': title, 'url': URL, 'links': links, 'categories': categories})
    except UnicodeEncodeError:
        recoded_links = []
        recoded_categories = []
        for l in links:       recoded_links.append(bytearray(l,'utf-16').decode('utf-16'))
        for c in categories:  recoded_categories.append(bytearray(c,'utf-16').decode('utf-16'))
        writer.writerow({'d_id': d_id, 'title': title, 'url': URL, 'links': recoded_links, 'categories': recoded_categories})

# Appends dataset to csv at path.
def append_test_data_csv(dataset: [[wr]], path):
    last_id = get_last_id(path)
    with open(path, 'a', newline='', encoding='utf-16') as file:
        # Header stuff, and starts writer.
        fieldnames = ['d_id', 'title', 'url', 'links', 'categories']
        w = csv.DictWriter(file, fieldnames=fieldnames)

        # For each path...
        d_id = last_id          # Distinguishes each path.
        for d in dataset:
            # Write each article...
            for a in d:
                safe_write(w, d_id, a.title, a.URL, a.links, a.categories)
            d_id += 1


# TODO: Would like to throw an exception if file doesn't exist.
def get_last_id(path):
    with open(path, 'r', newline='', encoding='utf-16') as file:
        return int(file.readlines()[-1].split(',')[0])


def read_test_data(path):
    with open(path, 'r', newline='') as csv:
        raise NotImplemented()
        # TODO: Need WikiRead to be separated into the web scraping controller and wiki model.



