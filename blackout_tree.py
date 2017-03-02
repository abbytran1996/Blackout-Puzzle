"""
Author: My Tran
File name: cpmpute.py
Purpose: Solve Black-out puzzle using Binary Tree. Prompt users for the number of blacked out squares.
"""


from btNode import *
from blackout import *


def make_tree( equation, value ):
    """
    Uses recursive call to make a binary tree whose leaves are all possible blacked out equation
    """
    if equation == '':
        left, right = None, None
    else:
        left = make_tree( equation[1:], value )
        right = make_tree( equation[1:], value + equation[0] )
    return BinaryTreeNode( left, value, right )


def solve_tree( tree, num ):
    """
    Uses recursive call to take each leaf and evaluate it.
    :returns: True if there is a solution.
              Else: returns None
    """
    if tree == None:
        return None
    #keep the boolean in 'solution' variable so that it wouldn't go away
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

def visit(tree, num):
    """
    Visits and evaluate if there is a leaf and there is a correct number of blacked out squares.
    Print out if there is a solution.
    :returns True if there is. Or else, returns None
    """
    if not tree.hasLeftChild() and not tree.hasRightChild() and len(tree.value) == num :
        result = test( tree.value )
        if result == True:
            print("Found solution: ", tree.value)
            return True

def main():
    """
    Prompts users for the file and and the number of blacked out squares.
    If there is no solution, print an announcement.
    """
    inFile = input('Enter the file')
    num = int(input('Enter the number of black out squares'))
    for line in open(inFile):
        equation = line.strip()
        print( 'Original equation:', equation)
        tree = make_tree( equation,'')
        result = solve_tree( tree, len(equation) - num)
        if result == None:
            print( "No solutions!" )

def test_make_tree():
    #Empty equation
    print( 'Test an empty equation:')
    expectedTree1 = BinaryTreeNode( None, '' , None)
    print( 'Makes like the expected?', make_tree('','') == expectedTree1)
    #Equation with just 1 element:
    print( 'Test an equation with just 1 element: "3" ')
    expectedTree2 = BinaryTreeNode( BinaryTreeNode( None, '', None ), '', BinaryTreeNode( None, '3', None) )
    print( 'Makes like the expected?', make_tree('3','') == expectedTree2)
    #Normal equation:
    print( 'Test: 2=5' )
    expectedTree3 = BinaryTreeNode( BinaryTreeNode( BinaryTreeNode( BinaryTreeNode( None, '', None ), '', BinaryTreeNode( None, '5', None)),
                    '', BinaryTreeNode( BinaryTreeNode( None, '=', None), '=', BinaryTreeNode( None, '=5', None ))), '', BinaryTreeNode( BinaryTreeNode( BinaryTreeNode( None, '2', None),
                    '2', BinaryTreeNode( None, '25', None)), '2', BinaryTreeNode( BinaryTreeNode( None, '2=', None), '2=', BinaryTreeNode( None, '2=5', None))))
    print( 'Makes like the expected?', make_tree('2=5','') == expectedTree3 )




if __name__ == "__main__":
    main()

"""
test_make_tree()
"""
