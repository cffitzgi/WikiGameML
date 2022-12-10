from WikiRead import WikiRead as wr
import csv


# Writes dataset to path.
def write_test_dat_csv(dataset: [[wr]], path):
    with open(path, 'w', newline='') as file:
        # Header stuff, and starts writer.
        fieldnames = ['d_id', 'title', 'url', 'links', 'categories']
        w = csv.DictWriter(file, fieldnames=fieldnames)
        w.writeheader()

        # For each path...
        d_id = 0            # Distinguishes each path.
        for d in dataset:
            # Write each article...
            for a in d:
                w.writerow({'d_id': d_id, 'title': a.title, 'url': a.URL, 'links': a.links, 'categories': a.categories})
            d_id += 1


# Appends dataset to csv at path.
def append_test_dat_csv(dataset: [[wr]], path):
    last_id = get_last_id(path)
    print(last_id)
    with open(path, 'a', newline='') as file:
        # Header stuff, and starts writer.
        fieldnames = ['d_id', 'title', 'url', 'links', 'categories']
        w = csv.DictWriter(file, fieldnames=fieldnames)

        # For each path...
        d_id = last_id          # Distinguishes each path.
        for d in dataset:
            # Write each article...
            for a in d:
                w.writerow({'d_id': d_id, 'title': a.title, 'url': a.URL, 'links': a.links, 'categories': a.categories})
            d_id += 1


# TODO: Would like to throw an exception if file doesn't exist.
def get_last_id(path):
    with open(path, 'r', newline='') as file:
        r = csv.reader(file)
        return int(list(r)[-1][0])


def read_test_data(path):
    with open(path, 'r', newline='') as csv:
        raise NotImplemented()
        # TODO: Need WikiRead to be separated into the web scraping controller and wiki model.



