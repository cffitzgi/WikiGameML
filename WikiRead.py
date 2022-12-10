from bs4 import BeautifulSoup as bs
import requests
import re


class WikiRead:
    links = None
    navigations = None
    categories = None
    def __init__(self, url):
        self.page = requests.get(url)
        self.soup = bs(self.page.content, "html.parser")

        self.URL = self.page.url
        self.title = self.get_page_title()

        self.soup = self.soup.find("div", id="content")

        self.links = self.get_page_links()          # Check to see if it contains the goal.
        #self.navigations = self.get_navigation()    # If categories are big match
        self.categories = self.get_categories()     # Heuristic GOAT (average similarity to goal categories)

    def __str__(self):
        s = ""
        s += "Title: " + self.title
        s += "\nURL: " + self.URL
        s += "\nLinks: " + str(self.links)
        s += "\nCategories: " + str(self.categories)
        return s + "\n"

    def read(self):
        return self.title, self.URL, self.links, self.categories #,self.navigations

    def get_page_title(self):
        return self.soup.find("title").text[:-12]

    def get_page_links(self):
        if self.links is not None:
            return self.links

        content_raw = re.sub(r'id="See_also"(.*)', '', str(self.soup), flags=re.DOTALL).strip()
        content = bs(content_raw, 'html.parser')
        content_links = content.find_all("a", {"href": re.compile('/wiki/*')})
        links = []
        for l in content_links:
            link = l['href']
            if ":" not in link:
                links.append(l['href'][6:])

        self.links = links[3:]
        return links[3:]

    # [Deprecated] Content will be contained in links (few exceptions are not useful).
    def get_infobox(self):
        try:
            infobox = self.soup.find("table", {"class": re.compile('infobox *')})
            box_links = infobox.find_all("a", {"href": re.compile('/wiki/*')})
        except AttributeError:
            return None

        infobox_links = []
        for l in box_links:
            infobox_links.append(l['href'])

        return infobox_links


    # [Deprecated] Sidebars are not included in most articles and offer no useful additional links.
    def get_sidebars(self):
        try:
            raw_bar = self.soup.find("table", {"class": re.compile('sidebar *')})
            bar_links = raw_bar.find_all("a", {"href": re.compile('/wiki/*')})
        except AttributeError:
            return None

        sidebar_links = []
        for l in bar_links:
            sidebar_links.append(l['href'])

        return sidebar_links

    # Often overlaps, but not always, worth gathering.
    def get_navigation(self):
        if self.navigations is not None:
            return self.navigations

        navs_raw = self.soup.find_all("div", {"class": re.compile('navbox')})
        navs_stripped = re.sub(r'Help:Authority_control(.*)', '', str(navs_raw), flags=re.DOTALL).strip()
        nav = bs(navs_stripped, 'html.parser')
        nav = nav.find_all("a", {"href": re.compile('/wiki/*')})

        nav_links = []
        for n in nav:
            nav_links.append(n['href'])
            # nav_links += n.find_all("a", {"href": re.compile('/wiki/*')})

        self.navigations = nav_links
        return nav_links

    def get_categories(self):
        if self.categories is not None:
            return self.categories

        cat_raw = self.soup.find("div", id="mw-normal-catlinks")
        raw_links = cat_raw.find_all("a", {"href": re.compile('/wiki/*')})[1:]
        cat_links = []
        for l in raw_links:
            cat_links.append(l['href'][15:])

        self.categories = cat_links
        return cat_links

def full_category(short_category):
    return "https://en.wikipedia.org/wiki/Category:" + short_category

def full_link(short_link):
    return "https://en.wikipedia.org/wiki/" + short_link


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