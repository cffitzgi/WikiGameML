from WikiScrape import WikiRead as wr
import WikiScrape
import GenTestData
import IO
import CategoryHeuristic as ch
import demo

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
    print(ch.category_heuristic("Former_kingdoms_in_Ireland", "Kingdom_of_Sicily"))  # 2
    print(ch.category_heuristic("Former_kingdoms_in_Ireland", "Fictional_kingdoms")) # 3
    print(ch.category_heuristic("Former_kingdoms_in_Ireland", "Chieftainships"))     # 4
    print(ch.category_heuristic("Former_kingdoms_in_Ireland", "Monarchies"))         # 3
