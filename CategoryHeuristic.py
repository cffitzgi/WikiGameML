import WikiRead
from WikiRead import CategoryRead as cr


TOP = "https://en.wikipedia.org/wiki/Category:Main_topic_classifications"

def flatten(l):
    return [item for sublist in l for item in sublist]

def CategoryHeuristic(c1, c2):
    cat1 = cr(c1)
    cat2 = cr(c2)

    cat1_all = [[cat1.title]]
    cat2_all = [[cat2.title]]

    f_cat1 = [cat1.title]
    f_cat2 = [cat2.title]

    while set(f_cat1).isdisjoint(f_cat2):

        if TOP not in f_cat1:
            new_step = []
            for c in cat1_all[-1]:
                cat1 = cr(c)
                for p in cat1.parent_categories:
                    new_step.append(p)
            cat1_all.append(new_step)
            f_cat1 += new_step

        if TOP not in f_cat1:
            new_step = []
            for c in cat2_all[-1]:
                cat2 = cr(c)
                for p in cat2.parent_categories:
                    new_step.append(p)
            cat2_all.append(new_step)
            f_cat2 += new_step

    h_val = 0
    common_ancestor = list(set(f_cat1).intersection(f_cat2))[0] #
    for step in cat1_all:
        if common_ancestor in step:
            break
        h_val += 1

    for step in cat2_all:
        if common_ancestor in step:
            break
        h_val += 1

    return h_val






