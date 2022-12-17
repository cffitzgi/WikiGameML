from bs4 import BeautifulSoup as bs
import requests
import re

RANDOM = "https://en.wikipedia.org/wiki/Special:Random"
TOP_CAT = "https://en.wikipedia.org/wiki/Category:Main_topic_classifications"

# TODO: Look into Wikipedia's edit page to read an article's unformatted text content.

# TODO: Split into the scrapper controller class and a data model class.

class CategoryRead:
    title = None
    url = None
    parent_categories = None
    subcategories = None
    articles = None

    def __init__(self, title):
        self.title = title
        self.url = full_category(title)

        self.page = requests.get(self.url)
        self.soup = bs(self.page.content, "html.parser")

        self.get_subcategories()
        self.get_parent_categories()
        # self.get_articles()

    def get_subcategories(self):
        if self.subcategories is not None: return self.subcategories

        try:
            raw = self.soup.find("div", id="mw-subcategories")
            cats_raw = raw.find_all("a", {"href": re.compile('/wiki/Category:*')})
        except AttributeError:
            self.subcategories = []
            return self.subcategories

        cats = []
        for c in cats_raw:
            cats.append(c['href'][15:])

        self.subcategories = cats
        return self.subcategories

    def get_parent_categories(self):
        if self.parent_categories is not None: return self.parent_categories
        if self.url == TOP_CAT:
            self.parent_categories = []
            return self.parent_categories

        raw = self.soup.find("div", id="mw-normal-catlinks")
        cats_raw = raw.find_all("a", {"href": re.compile('/wiki/Category:*')})
        cats = []
        for c in cats_raw:
            cats.append(c['href'][15:])

        self.parent_categories = cats
        return self.parent_categories

    def get_articles(self):
        if self.articles is not None: return self.articles

        raw = self.soup.find("div", id="mw-category mw-category-columns")
        articles_raw = raw.find_all("a", {"href": re.compile('/wiki/*')})
        articles = []
        for a in articles_raw:
            if ":" not in a['href']:
                articles.append(a['href'][6:])

        self.articles = articles
        return self.articles

class WikiRead:
    title = None
    url = None
    links = None
    categories = None

    def __init__(self, url):
        self.page = requests.get(url)
        self.soup = bs(self.page.content, "html.parser")

        self.URL = self.page.url
        self.title = self.get_page_title()

        self.soup = self.soup.find("div", id="content")

        self.links = self.get_page_links()          # Check to see if it contains the goal.
        self.categories = self.get_categories()     # Heuristic GOAT (average similarity to goal categories)

    def __str__(self):
        s = ""
        s += "Title: " + self.title
        s += "\nURL: " + self.URL
        s += "\nLinks: " + str(self.links)
        s += "\nCategories: " + str(self.categories)
        return s + "\n"

    # Returns all relevant information as tuple
    def read(self):
        return self.title, self.URL, self.links, self.categories

    # Returns or finds
    def get_page_title(self):
        if self.title is None:
            self.title = self.soup.find("title").text[:-12]
        return self.title

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
        return self.links

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

    # [Deprecated] Often overlaps with links, but not always.
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

    # Gets articles wikipedia categories.
    def get_categories(self):
        if self.categories is not None:
            return self.categories
        try:
            cat_raw = self.soup.find("div", id="mw-normal-catlinks")
            raw_links = cat_raw.find_all("a", {"href": re.compile('/wiki/*')})[1:]
        except AttributeError:
            return []
        cat_links = []
        for l in raw_links:
            cat_links.append(l['href'][15:])

        self.categories = cat_links
        return cat_links


# Formats category to be full wikipedia link
def full_category(short_category):
    return "https://en.wikipedia.org/wiki/Category:" + short_category


# Formats link id to be full wikipedia link.
def full_link(short_link):
    return "https://en.wikipedia.org/wiki/" + short_link


# Determines how much overlap is between list1 and list2
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
