import requests
import IO
import ArticleController

#runs demo
def run_demo(graph_map):
    #collect start and end URL's for game
    starting_article = input("Please enter a Wikipedia URL to start from...")
    target_article = input("Please enter a Wikipedia URL to end with...")
    #if starting_article is not a valid link?
    try:
        requests.get(starting_article)
        requests.get(target_article)
    except:
        print("Invalid URL") #ask again
        exit()
    check = 0
    starting_vertex = {}
    ending_vertex = {}
    for vertex in graph_map.get_vertices():
        if not starting_vertex:
            if vertex.url == starting_article:
                starting_vertex = vertex
                check = check + 1
        if not ending_vertex:
            if vertex.url == target_article:
                ending_vertex = vertex
                check = check + 1
        if check == 2:
            continue
    if check == 2:
            #run A* search over current database
        cost, path = astar(starting_vertex, ending_vertex)
            #print path
        print("astar: " + path)
    else:
        print("One or both articles do not exist in the dataset")

    #if starting_article is not already in database?
        #do 3-deep wiki search from connected articles (i.e. add all to database)
    #if target_article is not already in database?
        #do 3-deep wiki search from connected articles (i.e. add all to database)

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
    #read data from csv file
vertices = IO.read_test_data("1-data_set.csv")
    #check that data is read correctly
if len(vertices) > 0:
        #assemble the graph
    graph = ArticleController.Controller.AssembleGraph(vertices)
        #run the demo
    run_demo(graph)
else: #we effed up
    print("Error. Dataset not found.")
