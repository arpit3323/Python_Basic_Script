def remove_negatives(x):
    return True if x >= 0 else False
    
a = [-10, 27, 1000, -1, 0, -30]
[x for x in filter(remove_negatives, a)]
