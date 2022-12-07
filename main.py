import wikipedia as w
from bs4 import BeautifulSoup as bs
import requests
import re
from WikiRead import WikiRead

def get_page_links(s: bs):
    content_raw = re.sub(r'id="See_also"(.*)', '', str(s), flags=re.DOTALL).strip()
    content = bs(content_raw, 'html.parser')
    content_links = content.find_all("a", {"href": re.compile('/wiki/*')})
    links = []
    for l in content_links:
        links.append(l['href'])

    return links[3:]

def get_infobox(s:bs):
    return s.find("table", {"class": re.compile('infobox *')})

def get_sidebars(s:bs):
    raw_bar = s.find("table", {"class": re.compile('sidebar *')})
    bar_links = raw_bar.find_all("a", {"href": re.compile('/wiki/*')})

    sidebar_links = []
    for l in bar_links:
        sidebar_links.append(l['href'])

    return sidebar_links
    #return s.find_all("table", {"class": re.compile('sidebar *')} )

def get_navigation(s:bs):
    navs_raw = s.find_all("div", {"class": re.compile('navbox')} )
    navs_stripped = re.sub(r'Help:Authority_control(.*)', '', str(navs_raw), flags=re.DOTALL).strip()
    nav = bs(navs_stripped, 'html.parser')
    nav = nav.find_all("a", {"href": re.compile('/wiki/*')})

    nav_links = []
    for n in nav:
        nav_links.append(n['href'])
        #nav_links += n.find_all("a", {"href": re.compile('/wiki/*')})
    return nav_links

def get_categories(s:bs):
    cat_raw = s.find("div", id="mw-normal-catlinks")
    raw_links = cat_raw.find_all("a", {"href": re.compile('/wiki/*')})[1:]
    cat_links = []
    for l in raw_links:
        cat_links.append(l['href'])
    return cat_links


def how_useless(l1, l2):
    if l1 is None:
        print("List 1 is not a list")
        return
    if l2 is None:
        print("List 2 is not a list")
        return

    print(f'1st List Count: {len(l1)}')
    print(f'2nd List Count: {len(l2)}')
    count = 0
    unique = []
    for n in l2:
        if n in l1:
            count += 1
        else:
            unique.append(n)
    print(f'Overlap: {count}')
    print(unique)

if __name__ == '__main__':
    #URL = "https://en.wikipedia.org/wiki/Kevin_Bacon"
    #URL = "https://en.wikipedia.org/wiki/Wikipedia"
    #URL = "https://en.wikipedia.org/wiki/World_War_II"
    article = WikiRead("https://en.wikipedia.org/wiki/Special:Random")
    #article = WikiRead("https://en.wikipedia.org/wiki/World_War_II")
    #article = WikiRead("https://en.wikipedia.org/wiki/Ang_Mo_Kio")

    title = article.title
    url = article.URL
    links = article.links
    sidebars = article.get_sidebars()
    navigations = article.get_navigation()
    categories = article.get_categories()
    print(title)
    print(url)
    print(links)
    print(navigations)
    print(categories)
    how_useless(links, categories)

    exit()
    links = article.get_page_links()
    for l in links:
        print(l)
    exit()

    hitler = WikiRead("https://en.wikipedia.org/wiki/Adolf_Hitler")
    wwii = WikiRead("https://en.wikipedia.org/wiki/World_War_II")

    h_categories = hitler.get_categories()
    w_categories = wwii.get_categories()

    print("Hitler Categories")
    for c in h_categories:
        print(c)

    print("WWII Categories")
    for c in w_categories:
        print(c)

    # TODO: Exception check for articles that don't contain navigations.
    #   Brainstorm AI implementation beyond search.
    #   How to rank which content links should be checked.
    #       Is going through categories cheating???

    # Pointless (already in links)
    #infobox = get_infobox(soup)
    #sidebars = get_sidebars(soup)

