#return from the very FIRST recursive call
"""
def solve_tree( tree, num ):

    Uses recursive call to take each leaf and evaluate it.
    :returns: True if there is a solution.
              Else: returns None

    if tree == None:
        return None
    #keep the boolean in 'solution' variable so that it wouldn't go away
    #the 'solution' variable will carry the boolean result to the first REcursive Call!
    solution = solve_tree(tree.left, num)

    if solution != True:
        solution = solve_tree(tree.right, num)
    else:
        #if we found a solution already, don't assign it again amymore:
        solve_tree(tree.right, num)

    if solution != True:
        solution = visit(tree, num)

    else:
        #if we found a solution already, don't assign it again amymore:
        visit(tree, num)

    return solution
"""
from blackout import *
print( compute( '28-11') )