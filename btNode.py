
"""
Demonstrates simple binary tree node.
file: btNode.py
language: python3
Author: Scott C Johnson
"""

from rit_lib import *

class BinaryTreeNode(struct):
    """ A BinaryTreeNode has a value.
        A left child that is a BinaryTreeNode or None
        A right child that is a BinaryTreeNode or None
    """
    _slots = (((NoneType, 'BinaryTreeNode'), 'left'),
              (object, 'value'),
              ((NoneType, 'BinaryTreeNode'), 'right'))

    def isLeaf(self):
        """
        Returns if this node is a leaf node
        :return: True if it is a leaf node, False if it is not
        """
        if not self.hasLeftChild() and not self.hasRightChild():
            return True
        else:
            return False

    def getValue(self):
        """
        Gets the value of this node
        :return: the value of this node
        """
        return self.value

    def hasLeftChild(self):
        """
        Returns if this node has a left child
        :return: True if this node has a left child, False otherwise
        """
        return self.left != None

    def hasRightChild(self):
        """
        Returns if this node has a right child
        :return: True if this node has a right child, False otherwise
        """
        return self.right != None


    def bstNodeToString(self):
        """
        :return: the string representing the BinaryTree
                 with this node as the root
        """
        return (self.left.bstNodeToString() if self.hasLeftChild() else "")  +  \
              ( str( self.getValue() ) + ' ' ) + \
               (self.right.bstNodeToString() if self.hasRightChild() else "")

