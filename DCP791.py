# Write a function, throw_dice(N, faces, total), that determines how many ways it is 
# possible to throw N dice with some number of faces each to get a specific total.

# For example, throw_dice(3, 6, 7) should equal 15.

def throw_dice(N=int, faces=int, total=int) -> int:
    faceValues = list(range(1, faces+1))
    
    return 0
    
throw_dice(1, 5, 5)