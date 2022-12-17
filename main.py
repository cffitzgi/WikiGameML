from DataGen import GenTestData
from DataGen import IO
from Agent import CategoryHeuristic as ch
from Network import ArticleController as c


RANDOM = "https://en.wikipedia.org/wiki/Special:Random"


def making_bacon(size, k, n):
    print("Generating Bacon Paths...", end='')
    bacon = GenTestData.gen_raw_test_data(size, k, n, starting_link="https://en.wikipedia.org/wiki/Kevin_Bacon")
    print("done\nWriting Bacon Paths...", end='')
    IO.write_test_data_csv(bacon, 'bacon.csv')
    print("done")
    return bacon

def TestDataGeneration(out_file, datasetsize=50, min_articles=[50, 100, 150, 200], path_length=[3, 4, 5, 6, 7]):
    GenTestData.add_testdata_file(out_file, datasetsize, min_articles, path_length)


if __name__ == '__main__':
    network = c.ReadNetwork("TestSave.json")

    exit()
        #read data from csv file
    articles = IO.read_test_data("1-data_set.csv")
        #check that data is read correctly
    if len(articles) > 0:
            #assemble the network
        net = c.AssembleNetwork(articles)
        c.WriteNetwork("TestSave.json", net)
    else: #we effed up
        print("Error. Dataset not found.")
