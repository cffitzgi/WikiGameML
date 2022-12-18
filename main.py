from DataGen import GenTestData
from DataGen import IO
from Agent import CategoryHeuristic as ch
from Network import ArticleController as c
from Agent.WikiGamePlayer import Agent


RANDOM = "https://en.wikipedia.org/wiki/Special:Random"

generated_data_csv = "1-data_set.csv"
saved_network_json = "article_network.json"

def making_bacon(size, k, n):
    print("Generating Bacon Paths...", end='')
    bacon = GenTestData.gen_raw_test_data(size, k, n, starting_link="https://en.wikipedia.org/wiki/Kevin_Bacon")
    print("done\nWriting Bacon Paths...", end='')
    IO.write_test_data_csv(bacon, 'bacon.csv')
    print("done")
    return bacon

def TestDataGeneration(out_file, datasetsize=50, min_articles=[50, 100, 150, 200], path_length=[3, 4, 5, 6, 7]):
    GenTestData.add_testdata_file(out_file, datasetsize, min_articles, path_length)

def load_network():
    net = None
    inp = input("[R]ead existing network\n"
                "[G]enerate new network\n"
                "E[x]it\n> ")
    if inp.capitalize() == 'R':
        try:
            net = c.ReadNetwork(saved_network_json)
        except FileNotFoundError:
            print("Error: File does not exist. Generate network first.")

    elif inp.capitalize() == 'G':
        articles = IO.read_test_data(generated_data_csv)
        net = c.AssembleNetwork(articles)

        inp = input("[W]rite this network?")
        if inp.capitalize() == 'W':
            c.WriteNetwork(saved_network_json, net)
    elif inp.capitalize() == 'X':
        print("Goodbye")
        exit()

    else:
        print("Invalid input... ")

    return net


if __name__ == '__main__':
    network = None
    while network is None:
        network = load_network()


