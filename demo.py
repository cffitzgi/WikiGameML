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

def astar(starting_node, goal_node):
    # complete the function body: f = g + h
    path = {}
    path[starting_node.g] = starting_node
    paths = {}
    cost = 0
    if starting_node == goal_node:
        tempCost = starting_node.h + starting_node.g
        return tempCost, path
    children = starting_node.connected_to
    for x in children:
        tempCost, tempPath = astar(x, goal_node)
        if tempPath is not None:
            f = tempCost
            f_limit = cost
            if tempCost < f_limit:
                f_limit = tempCost
            path[x.g] = tempPath
            paths[x.g] = [tempCost, path]
    if len(paths) > 0:
        cost = 1000000
        for a in paths:
            if paths[a][0] <= cost:
                cost = paths[a][0]
        for a in paths:
            if paths[a][0] == cost:
                return (a,paths[a][0])

    print('No Path Found')
    return None, None
