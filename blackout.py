"""
Author: My Tran
File name: cpmpute.py
Purpose: Solve Black-out puzzle using Stack and Queue. 2 black-out squares.
"""

from number import *
from operation import *


def calculate( numStack, operStack ):
    """
    Takes the first two numbers from the numStack and the first operation from the operStack
    Does the calculation.
    """
    num1 = topNumber(numStack)
    numStack = popNumber( numStack )
    num2 = topNumber(numStack)
    numStack = popNumber( numStack )
    oper = topOperation( operStack )
    operStack = popOperation( operStack )
    if oper == '+':
        return num1 + num2, numStack, operStack
    elif oper == '-':
        return num2 - num1, numStack, operStack
    elif oper == '*':
        return num1 * num2, numStack, operStack
    elif oper == '/':
        #Divides by 0
        if num1 == 0:
            return None, numStack, operStack
        return num2 / num1, numStack, operStack



def compute( equation ):
    """
    Takes each side of the equation, compute if it valid.
    :returns: the result
              If it's not valid, returns None.
    """
    number = ''
    numStack = None
    operStack = None
    for i in equation:
        if i.isdigit():
            #form a number of any length:
            number += i
        elif i in ['+', '-', '*', '/']:
            if number == '':
                return None
            numStack = pushNumber( numStack, int(number) )
            number = ''
            #Check if the numStack is empty or not:
            operation = checkOperation( i )
            if isEmpty( operStack ):
                operStack = pushOperation( operStack, operation )
            else:
                topPre = topPrecedence( operStack )
                if topPre >= operation.precedence:
                    #Before calculating, always check the numStack again:
                    if size(numStack) <=1:
                        return None
                    result, numStack, operStack = calculate( numStack, operStack )
                    if result == None:
                        return None
                    numStack = pushNumber( numStack, result )
                operStack = pushOperation( operStack, operation)

        elif i == '(':
            operation = Operation( i, 0 )
            operStack = pushOperation( operStack, operation)
            #In case 12(56+3)
            if number != '':
                return None

        elif i == ')':
            #In case: 6+5-)
            if number == '':
                return None
            numStack = pushNumber( numStack, int(number) )
            number = ''
            # For example: 12) + 5 - 6
            if isEmpty(operStack):
                return None
            while topPrecedence( operStack ) != 0 :
                if size(numStack) <=1:
                    return None
                result, numStack, operStack = calculate( numStack, operStack )
                if result == None:
                    return None
                numStack = pushNumber( numStack, result )
                #In case there is no '(':
                if isEmpty( operStack ):
                    return None
            #Pop the '(' out of the operStack:
            operStack = popOperation( operStack )
    #Push the last number to the numStack:
    if number != '':
        numStack = pushNumber( numStack, int(number) )
    while not isEmpty(operStack) and not isEmpty(numStack):
        if topPrecedence(operStack) == 0:
            return None
        if size(numStack) <=1 and not isEmpty(operStack):
            return None
        result, numStack, operStack = calculate( numStack, operStack )
        if result == None:
            return None
        numStack = pushNumber( numStack, result )
    #The operStack is empty but there are more than one final number in the numStack:
    if isEmpty(operStack) and size( numStack ) != 1:
        return None
    return numStack.top.number


def test( equation ):
    """
    Tests if the equation has a valid form. If yes, computes each side and compares them.
    :returns: True if there is a solution
              Else: returns False.
    """
    if "=" in equation:
        if equation.find('=') != 0 and equation.find( '=' ) != (len(equation) - 1) :
            expression = equation.split('=')
            leftResult, rightResult = compute( expression[0] ) , compute( expression[1] )
            if leftResult == None or rightResult == None:
                return False
            elif leftResult == rightResult:
                return True
            else:
                return False
        else:
                return False
    else:
        return False

def solve( equation ):
    """
    Black out 2 squares in the equation.
    :returns: The correct blacked function.
              Or else returns None.
    """
    for i in range( 0, len(equation) ):
        newEquation1 = equation[:i] + equation[i+1:]
        for j in range( i , len(newEquation1) ):
            newEquation2 = newEquation1[:j] + newEquation1[j+1:]
            result = test(newEquation2)
            if result == True:
                return newEquation2
    return None


def main():
    """
    Prompt users for the file name.
    Execute Black out functions on each line in the file.
    :returns: Solution if there is one, else inform that cannot find.
    """
    inFile = input('Enter the file')
    for line in open(inFile):
        equation = line.strip()
        print( 'Original puzzle:', equation)
        solved = solve( equation )
        if solved != None:
            print( 'Found solution:', solved)
            print('\n')
        else:
            print( 'Cannot find any solutions.')
            print('\n')

##############
#         TESTING
##############

def compute_tests():
    #Calculate operation with a higher precedence first:
    print( 'Compute: 2 + 3 * 6')
    print( 'Result is 20?', compute('2+3*6') == 20)
    print('\n')
    #Calculate in () first:
    print( 'Compute: 2 * (3 + 6)')
    print( 'Result is 18?', compute('2*(3+6)') == 18)
    print('\n')
    #Multi-digit numbers:
    print( 'Compute: 2 + 10 - 36')
    print( 'Result is -24?', compute('2+10-36') == -24)
    print('\n')
    #Equation with '(' but no ')':
    print( 'Compute: (12 + 3 - 6')
    print( 'No result?', compute('(12+3-6') == None)
    print('\n')
    #Equation with ')' but no '(':
    print( 'Compute: 12 + 3) - 6')
    print( 'No result?', compute('12+3)-6') == None)
    print('\n')
    #Equation with an operation at the beginning:
    print( 'Compute: + 12 - 6')
    print( 'No result?', compute('+12-6') == None)
    print('\n')
    #Equation with an operation at the end:
    print( 'Compute: 12 - 6 +')
    print( 'No result?', compute('12-6+') == None)
    print('\n')
    #Equation with two operations are next to each other:
    print( 'Compute: 12 + - 6')
    print( 'No result?', compute('12+-6') == None)
    print('\n')
    #No operation before '(' or after ')':
    print( 'Compute: 6(2 + 3) and (2 + 3)6')
    print( 'Both no result?', compute('6(2 + 3)') == None, compute('(2 + 3)6') == None)
    print('\n')


def test_tests():
    #Normal function:
    print( 'Test: 5 + 2 = 3 + 6')
    print( 'Valid but wrong?', test('5+2=3+6') == False)
    print('\n')
    #Normal function:
    print( 'Test: 5 + 4 = 3 + 6')
    print( 'Valid but right?', test('5+4=3+6') == True)
    print('\n')
    #Equation with '=' at the beginning:
    print( 'Test: = 5 + 2')
    print( 'Invalid?', test('=5+2') == False)
    print('\n')
    #Equation with '=' at the end:
    print( 'Test: 5 + 2 =')
    print( 'Invalid?', test('5+2=') == False)
    print('\n')
    #Equation with no '=':
    print( 'Test: 5 + 2 - 3')
    print( 'Invalid?', test('5+2-3') == False)
    print('\n')

def solve_tests():
    #Empty equation:
    print( 'Solve an empty equation.')
    print( 'Invalid?', solve('') == None)
    print('\n')
    #Equation with one or two elements:
    print( 'Solve: "3", "3+"')
    print( 'Both invalid?', solve('3') == None, solve('3+') == None )
    print('\n')
    #Normal equation:
    print( 'Solve: 3+2=6')
    print( 'No solution?', solve('3+2=6') == None )
    print('\n')
    #Normal equation:
    print( 'Solve: 3+2=3')
    print( 'Solution:', solve('3+2=3'))
    print('\n')



if __name__ == "__main__":
   main()

"""
#Run testing functions
compute_tests()
test_tests()
solve_tests()
"""















