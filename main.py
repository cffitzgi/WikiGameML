from WikiRead import WikiRead as wr
import WikiRead
import GenTestData
from GenTestData import GenTestData as gen
import IO

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

    raw_data = GenTestData.gen_raw_test_data(50, 50, 3)
    IO.write_test_dat_csv(raw_data, 'data_1.csv')
    raw_data = GenTestData.gen_raw_test_data(50, 100, 3)
    IO.append_test_dat_csv(raw_data, 'data_1.csv')
    raw_data = GenTestData.gen_raw_test_data(50, 50, 5)
    IO.append_test_dat_csv(raw_data, 'data_1.csv')
    raw_data = GenTestData.gen_raw_test_data(50, 100, 5)
    IO.append_test_dat_csv(raw_data, 'data_1.csv')
    raw_data = GenTestData.gen_raw_test_data(50, 50, 10)
    IO.append_test_dat_csv(raw_data, 'data_1.csv')
    raw_data = GenTestData.gen_raw_test_data(50, 100, 10)
    IO.append_test_dat_csv(raw_data, 'data_1.csv')

    #collect start and end URL's for game
    starting_article = input("Please enter a Wikipedia URL to start from...")
    target_article = input("Please enter a Wikipedia URL to end with...")
    #if starting_article is not a valid link?
        #starting_article = input("Please enter a Wikipedia URL to start from...") #ask again
    #if target_article is not a valid link?
        #target_article = input("Please enter a Wikipedia URL to end with...") #ask again
    #if starting_article is not already in database?
        #do 3-deep search from connected articles (i.e. add all to database)
    #if target_article is not already in database?
        #do 3-deep search from connected articles (i.e. add all to database)
    n = 5 #initial depth from starting_article
    #start loop:
        #run A* search
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
    IO.write_test_dat_csv(raw_data, 'test.csv')
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


