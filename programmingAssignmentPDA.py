"""
Created on Sat Jan  2 12:24:52 2021

@author: mcaptain79
"""
#implementation of DPDA
def DPDA(myStr,currentState):
    n = len(myStr)
    stack = ['z']
    for i in range(n):
        if(currentState == 'q0' and myStr[i] == 'a' and stack.pop() == 'z'):
            currentState = 'q1'
            stack.append('z')
            stack.append('a')
        elif(currentState == 'q1' and myStr[i] == 'a' and stack.pop() == 'a'):
            stack.append('a')
            stack.append('a')
        elif(currentState == 'q1' and myStr[i] == 'b' and stack.pop() == 'a'):
            currentState = 'q2'
        elif(currentState == 'q2' and myStr[i] == 'b' and stack.pop() == 'a'):
            currentState = 'q2'
        else:
            return False
    if(currentState == 'q2' and stack.pop() == 'z'):
        return True
    else:
        #print(stack,currentState)
        return False
print('testing DPDA')
print('a',DPDA('a','q0'))
print('b',DPDA('b','q0'))
print('aabb',DPDA('aabb','q0'))
print('bbbaaa',DPDA('bbbaaa','q0'))
print('abab',DPDA('abab','q0'))
print('bbb',DPDA('bbb','q0'))
print('aaaabbbb',DPDA('aaaabbbb','q0'))
print('-----------------------------------------------')
def NPDA(myStr):
    n = len(myStr)
    for i in range(1,n):
        str1 = myStr[:i]
        str2 = myStr[i:]
        if str1 == str2[::-1]:
            return True
    return False
print('testing NPDA')
print('a',NPDA('a'))
print('ab',NPDA('ab'))
print('abba',NPDA('abba'))
print('aaaa',NPDA('aaaa'))
print('aaa',NPDA('aaa'))
        
    

