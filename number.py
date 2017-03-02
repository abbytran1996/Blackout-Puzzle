"""
Author: My Tran
File name: number.py
Purpose: Define Number class
"""

from rit_lib import *

class Number(struct):
    _slots = ( (int, float),'number' )

class NumberStack(struct):
    _slots = ( (Number,'top'), ((NoneType,'NumberStack'),'next') )

def isEmpty(stack):
    return stack == None

def size(stack):
    if isEmpty(stack):
        return 0
    else:
        return 1 + size(popNumber(stack))

def topNumber(stack):
    return stack.top.number

def pushNumber( stack , number ):
    if number == '':
        return None
    return NumberStack( Number( number ), stack )

def popNumber( stack ):
    """
        Return the INTEGER at the top of the stack
        Pop that Number class out of the ttack.
    """
    return stack.next










