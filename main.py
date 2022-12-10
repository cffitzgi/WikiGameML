from WikiRead import WikiRead as wr
import WikiRead
import GenTestData
from GenTestData import GenTestData as gen
import IO
import requests

RANDOM = "https://en.wikipedia.org/wiki/Special:Random"



if __name__ == '__main__':
    # Quick debugging reference for WikiRead.
    #article = wr("https://en.wikipedia.org/wiki/Special:Random")
    #article = wr("https://en.wikipedia.org/wiki/Adolf_Hitler")
    #article = wr("https://en.wikipedia.org/wiki/World_War_II")
    #article = wr("https://en.wikipedia.org/wiki/Ang_Mo_Kio")
    #article = wr("https://en.wikipedia.org/wiki/Kevin_Bacon")
    #article = wr("https://en.wikipedia.org/wiki/Wikipedia")

    #raw_data = gen("https://en.wikipedia.org/wiki/Adolf_Hitler", 50, 5).gen()
    #IO.write_test_dat_csv([raw_data], 'test.csv')

    out_file = 'datatest.csv'

    #GenTestData.gen_testdata_file(out_file, 50, [50, 100], [3, 5, 10])
    #exit()

    print("Reading Dataset 1...", end='')
    raw_data = GenTestData.gen_raw_test_data(50, 50, 3)
    print("done\nWriting Dataset 1...", end='')
    IO.write_test_data_csv(raw_data, out_file)

    print("done\nReading Dataset 2...", end='')
    raw_data = GenTestData.gen_raw_test_data(50, 100, 3)
    print("done\nWriting Dataset 2...", end='')
    IO.append_test_data_csv(raw_data, out_file)
    print("done")

    #exit()

    print("done\nReading Dataset 3...", end='')
    raw_data = GenTestData.gen_raw_test_data(50, 50, 5)
    print("done\nWriting Dataset 3...", end='')
    IO.append_test_data_csv(raw_data, out_file)

    print("done\nReading Dataset 4...", end='')
    raw_data = GenTestData.gen_raw_test_data(50, 100, 5)
    print("done\nWriting Dataset 4...", end='')
    IO.append_test_data_csv(raw_data, out_file)

    print("done\nReading Dataset 5...", end='')
    raw_data = GenTestData.gen_raw_test_data(50, 50, 10)
    print("done\nWriting Dataset 5...", end='')
    IO.append_test_data_csv(raw_data, out_file)

    print("done\nReading Dataset 6...", end='')
    raw_data = GenTestData.gen_raw_test_data(50, 100, 10)
    print("done\nWriting Dataset 6...", end='')
    IO.append_test_data_csv(raw_data, out_file)
    print("done")

    #collect start and end URL's for game
    starting_article = input("Please enter a Wikipedia URL to start from...")
    target_article = input("Please enter a Wikipedia URL to end with...")
    #if starting_article is not a valid link?
    try:
        page = requests.get(starting_article)
        page2 = requests.get(target_article)
    except:
        print("Invalid URL") #ask again
        exit()
    #if starting_article is not already in database?
        #do 3-deep search from connected articles (i.e. add all to database)
    #if target_article is not already in database?
        #do 3-deep search from connected articles (i.e. add all to database)
    n = 3 #initial depth from starting_article
    #add all articles n=3 deep to dataset, if not already searched
    #start loop:
        #run A* search over current database
        #if not found, expand to n+1 from starting_article

    exit()

    # Old debugging code that may be useful as a template later.
    ''' 
    raw_data.extend(GenTestData.gen_raw_test_data(50, 100, 3))
    raw_data.extend(GenTestData.gen_raw_test_data(50, 50, 5))
    raw_data.extend(GenTestData.gen_raw_test_data(50, 100, 5))
    raw_data.extend(GenTestData.gen_raw_test_data(50, 50, 10))
    raw_data.extend(GenTestData.gen_raw_test_data(50, 100, 10))
    '''
    IO.write_test_data_csv(raw_data, 'test.csv')
    exit()

    # Generates multiple datasets.
    raw_data = GenTestData.gen_raw_test_data(5, 50, 5)
    n = 1
    for p in raw_data:
        print(f"Data #{n}")
        n += 1
        for a in p:
            print(str(a))
    exit()

    path = gen(RANDOM, 100, 5).gen()
    for p in path:
        print(p)


