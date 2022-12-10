import requests
def demo():
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
    #print path
    