from WikiRead import WikiRead as wr
import WikiRead
import GenTestData
import IO
import demo

RANDOM = "https://en.wikipedia.org/wiki/Special:Random"
out_file = 'datatest.csv'


def making_bacon(size, k, n):
    print("Generating Bacon Paths...", end='')
    bacon = GenTestData.gen_raw_test_data("https://en.wikipedia.org/wiki/Kevin_Bacon", size, k, n)
    print("done\nWriting Bacon Paths...", end='')
    IO.write_test_data_csv(bacon, 'bacon.csv')
    print("done")
    return bacon


if __name__ == '__main__':

    #demo.demo()
    #exit()

    # Quick debugging reference for WikiRead.
    #article = wr("https://en.wikipedia.org/wiki/Adolf_Hitler")
    #article = wr("https://en.wikipedia.org/wiki/World_War_II")
    #article = wr("https://en.wikipedia.org/wiki/Ang_Mo_Kio")
    #article = wr("https://en.wikipedia.org/wiki/Kevin_Bacon")
    #article = wr("https://en.wikipedia.org/wiki/Wikipedia")

    GenTestData.gen_testdata_file(out_file, 50, [50, 100], [3, 5, 10])
    exit()

    '''
    print("Generating Dataset 1...", end='')
    raw_data = GenTestData.gen_raw_test_data(50, 50, 3)
    print("done\nWriting Dataset 1...", end='')
    IO.write_test_data_csv(raw_data, out_file)

    print("done\nGenerating Dataset 2...", end='')
    raw_data = GenTestData.gen_raw_test_data(50, 100, 3)
    print("done\nWriting Dataset 2...", end='')
    IO.append_test_data_csv(raw_data, out_file)
    print("done")
    #'''

