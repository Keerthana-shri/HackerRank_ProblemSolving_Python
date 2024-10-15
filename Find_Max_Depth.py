maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    level = level + 1
    
    
    for e in elem:
        depth(e, level)
    if(level > maxdepth):
        maxdepth = level