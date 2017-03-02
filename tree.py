
from rit_lib import *
from treeNode import *

############################################################
# Class definiton
############################################################

class BinaryTree( struct ):
    """ A non-empty BinaryTree has a root BSTNode.
        A empty BinaryTree has a root of None
    """
    _slots = ((NoneType, BinaryTreeNode), 'root')

    def add(self, value):
        """ bstSearch: BinarySearchTree * Number -> NoneType
            Adds the value to the tree.
        """
        if self.root == None:
            self.root = BinaryTreeNode(None, value, None)
        else: # we can only add to a leaf node, so get to a leaf
            current = self.root
            while True:
                if value < current.value and current.left == None:
                    current.left = BinaryTreeNode(None, value, None)
                    break
                elif value < current.value:
                    current = current.left
                elif value >= current.value and current.right == None:
                    current.right = BinaryTreeNode(None, value, None)
                    break
                elif value >= current.value:
                    current = current.right

    ############################################################
    # String Conversion
    ############################################################

    def bstToString( self ):
        """ bstToString: BinarySearchTree -> String
            Converts the BST into a string for viewing
        """
        if self.root == None:
            return ''
        else:
            return self.root.bstNodeToString()

    def isEmpty( bst ):
        """ bstSearch: BinarySearchTree -> Boolean
            Returns if this CST is empty
        """
        return bst.root == None

    def bstSearch( self, value ):
        """ bstSearch: BinarySearchTree * Number -> Boolean
            Returns if the value exists in the BST
         """
        if self.isEmpty():
            return False
        else:
            current = self.root
            while value != current.value:
                if value < current.value and current.left == None:
                    return False
                elif value < current.value:
                    current = current.left
                elif value >= current.value and current.right == None:
                    return False
                elif value >= current.value:
                    current = current.right
            return True


def createBST():
    return BinaryTree(None)

############################################################
# Sample trees
############################################################




# Tests
def test_bstToString():
    """
    test_bstToString : Void -> None
    """
    print( 'Testing bstToString' )
    exampleTree1 = createBST()
    exampleTree1.add(1)
    print(exampleTree1)
    print( exampleTree1.bstToString( ) == '1 ')
    exampleTree1.add(3)
    print( exampleTree1.bstToString( ) == '1 3 ')
    exampleTree1.add(4)
    print( exampleTree1.bstToString( ) == '1 3 4 ')
    exampleTree1.add(5)
    exampleTree1.add(7)
    exampleTree1.add(6)
    exampleTree1.add(9)
    print( exampleTree1.bstToString( ) == '1 3 4 5 6 7 9 ' )


############################################################
# Search
############################################################

# Tests
def test_bstSearch():
    """
    test_bstSearch : Void -> None
    """
    exampleTree1 = createBST()
    exampleTree1.add(1)
    exampleTree1.add(4)
    exampleTree1.add(10)
    exampleTree1.add(5)
    exampleTree1.add(6)
    print( 'Testing bstSearch' )
    print( exampleTree1.bstSearch( 1 ) == True)
    print( exampleTree1.bstSearch( 3 ) == False )


# run tests

if __name__ == "__main__":
    test_bstToString()
    test_bstSearch()
