from WikiRead import WikiRead as wr
import WikiRead
import GenTestData
from GenTestData import GenTestData as gen


RANDOM = "https://en.wikipedia.org/wiki/Special:Random"



if __name__ == '__main__':
    article = None
    while article == None:
        try:
            article = wr("https://en.wikipedia.org/wiki/Special:Random")
        except GenTestData.TooFewOutgoingLinks:
            article = None
    #article = wr("https://en.wikipedia.org/wiki/Adolf_Hitler")
    #article = wr("https://en.wikipedia.org/wiki/World_War_II")
    #article = wr("https://en.wikipedia.org/wiki/Ang_Mo_Kio")
    #article = wr("https://en.wikipedia.org/wiki/Kevin_Bacon")
    #article = wr("https://en.wikipedia.org/wiki/Wikipedia")

    #print(str(article))

    path = gen(RANDOM, 100, 5).gen()
    for p in path:
        print(p)


    # TODO: Exception check for articles that don't contain navigations.
    #   Brainstorm AI implementation beyond search.
    #   How to rank which content links should be checked.
    #       Is going through categories cheating???


