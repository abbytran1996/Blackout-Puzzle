"""
Author: My Tran
File name: operation.py
Purpose: Define Operation class
"""
from rit_lib import *

class Operation(struct):
    _slots = ( (str,'operation'), (int,'precedence'))

class OperationStack(struct):
    _slots = ( (Operation,'top'), ((NoneType,'OperationStack'),'next') )

def isEmpty(stack):
    """
        Return if the stack is empty or not.
    """
    return stack == None

def pushOperation( stack, operation ):
    """
        Add a new Operation CLASS to the top of the stack
    """
    return OperationStack( operation, stack )

def topOperation( stack ):
    return stack.top.operation

def topPrecedence( stack ):
    """
        Return an INTEGER indicating the precedence of the operation at the top of the stack
    """
    return stack.top.precedence

def popOperation( stack ):
    """
        Return a STRING indicating the operation at the top of the stack.
        Then pop it out of the stack
    """
    return stack.next

def checkOperation( oper ):
    if oper == '+':
        return Operation( '+', 1 )
    elif oper == '-':
        return Operation( '-', 1 )
    elif oper == '*':
        return Operation( '*', 2 )
    elif oper == '/':
        return Operation( '/', 2 )



