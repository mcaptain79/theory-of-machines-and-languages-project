"""
Created on Sat Jan  2 10:50:00 2021

@author: mcaptain79
"""
#the code below is my implementation
"""
this DFA accepts a string if number of b is odd
                and its state are q0 and q1
"""
def DFA1(myString,currentState):
    if len(myString) == 0:
        if(currentState) == 'q1':
            return True
        else:
            return False
    if(myString[0] == 'a' and currentState == 'q0'):
        currentState = 'q0'
        return DFA1(myString[1:],currentState)
    elif(myString[0] == 'b' and currentState == 'q0'):
        currentState = 'q1'
        return DFA1(myString[1:],currentState)
    if(myString[0] == 'a' and currentState == 'q1'):
        currentState = 'q1'
        return DFA1(myString[1:],currentState)
    elif(myString[0] == 'b' and currentState == 'q1'):
        currentState = 'q0'
        return DFA1(myString[1:],currentState)
#initializing currentState with q0
def initialize1(myString):
    currentState = 'q0'
    return DFA1(myString,currentState)

#checking if this work properly
print('testing for DFA1')
print('abbba',initialize1('abbba'))
print('ababa',initialize1('ababa'))
print('aaaaaba',initialize1('aaaaaba'))
print('bbbbb',initialize1('bbbbb'))
print('bbbb',initialize1('bbbb'))
print('aaaaaaa',initialize1('aaaaaaa'))
print('--------------------------------------------------')
#this DFA accepts finite set if inputs
def DFA2(myStr):
    acceptanceList = ['a','ab','aaa','bbb','bbbb','abab']
    if myStr in acceptanceList:
        return True
    else:
        return False
print('testing for DFA2')
print('aaaaa',DFA2('aaaaa'))
print('abbaa',DFA2('abbaa'))
print('a',DFA2('a'))
print('ab',DFA2('ab'))
print('--------------------------------------------------')
#checing if two DFA accept the same input or not on some instances
print('checking some inputs for both DFAs')
if(initialize1('aaaaaaa') == True and DFA2('aaaaaaa') == True):
    print('aaaaaaa','acceptance')
else:
    print('aaaaaaa','not accepted')
if(initialize1('a') == True and DFA2('a') == True):
    print('a','acceptance')
else:
    print('a','not accepted')
if(initialize1('ab') == True and DFA2('ab') == True):
    print('ab','acceptance')
else:
    print('ab','not accepted')
if(initialize1('bbb') == True and DFA2('bbb') == True):
    print('bbb','acceptance')
else:
    print('bbb','not accepted')


