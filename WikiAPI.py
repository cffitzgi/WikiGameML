import pywikibot as w
import WikiScrape as wr


class PyWikiRead:
    title = None
    url = None
    links = None
    categories = None

    def __init__(self, url):
        self.site = w.Site('wikipedia:en')
        self.page = w.Page(site, url[30:])

        self.title = page.title(insite=True)
        self.url = url
        self.links = list(page.linkedPages(content=True))
        self.categories = list(map(clean_cat, page.categories(content=True)))


def clean_cat(s):
    return s[9:]



site = w.Site('wikipedia:en')
page = w.Page(site, u"Kevin_Bacon")
cats = list(page.categories(content=True))
links = list(page.linkedPages(content=True))

print(str(page.title(insite=True)))
print(page.full_url())
print(links)
print(cats)
exit()
