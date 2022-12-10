from WikiRead import WikiRead as wr
import WikiRead


RANDOM = "https://en.wikipedia.org/wiki/Special:Random"


def test_print(article: wr):
    title = article.title
    url = article.URL
    links = article.links
    sidebars = article.get_sidebars()
    navigations = article.get_navigation()
    categories = article.get_categories()
    print("Title:", title)
    print("URL:",url)
    print("Links:",links)
    print("Categories:",categories)


def full_category(short_category):
    return "https://en.wikipedia.org/wiki/Category:" + short_category


def full_link(short_link):
    return "https://en.wikipedia.org/wiki/" + short_link


if __name__ == '__main__':
    article = wr("https://en.wikipedia.org/wiki/Special:Random")
    #article = wr("https://en.wikipedia.org/wiki/Adolf_Hitler")
    #article = wr("https://en.wikipedia.org/wiki/World_War_II")
    #article = wr("https://en.wikipedia.org/wiki/Ang_Mo_Kio")
    #article = wr("https://en.wikipedia.org/wiki/Kevin_Bacon")
    #article = wr("https://en.wikipedia.org/wiki/Wikipedia")

    test_print(article)




    # TODO: Exception check for articles that don't contain navigations.
    #   Brainstorm AI implementation beyond search.
    #   How to rank which content links should be checked.
    #       Is going through categories cheating???


