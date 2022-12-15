from WikiRead import WikiRead as wr
import csv
import ArticleModel

dataset_count = 0


# Was encountering a lot of encoding errors when writing/reading, this insures not encoding errors.
def safe_write(writer, d_id, title, URL, links, categories):
    try:
        writer.writerow({'d_id': d_id, 'title': title, 'url': URL, 'links': links, 'categories': categories})
    except UnicodeEncodeError:
        recoded_links = []
        recoded_categories = []
        for l in links:       recoded_links.append(bytearray(l,'utf-16').decode('utf-16'))
        for c in categories:  recoded_categories.append(bytearray(c,'utf-16').decode('utf-16'))
        writer.writerow({'d_id': d_id, 'title': title, 'url': URL, 'links': recoded_links, 'categories': recoded_categories})


# (Over)writes dataset to path.
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


# Gets the last id used in the .csv at the given path.
def get_last_id(path):
    with open(path, 'r', newline='', encoding='utf-16') as file:
        return int(file.readlines()[-1].split(',')[0])

def read_test_data(path):
    with open(path, 'r', newline='', encoding='None') as dataset:
        reader = csv.reader(dataset, delimiter = ',')
        vertices = {}
        for row in reader:
            title = row["title"]
            url = row["url"]
            links = row["links"]
            categories = row["categories"]
            temp_vertex = ArticleModel.Vertex(title, url, links, categories)
            vertices[temp_vertex.id] += temp_vertex
        return vertices

        #header = next(reader)
        #data = np.array(list(reader)).astype(str)
        #return data
