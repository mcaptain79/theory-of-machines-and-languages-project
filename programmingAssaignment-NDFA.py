"""
Created on Sat Jan  2 11:37:56 2021

@author: mcaptain79
"""
#implentation of NDFA like a turing machine
def NDFA1(myStr):
    if(len(myStr) == 0):
        return False
    if(myStr[0] == 'a'):
        return True
    else:
        return False
print('NDFA1 test')
print('aaaa',NDFA1('aaaa'))
print('bbbb',NDFA1('bbbb'))
print('abbb',NDFA1('abbb'))
print('baaa',NDFA1('baaa'))
print('',NDFA1(''))
def NDFA2(myStr):
    if 'a' in myStr:
        return False
    else:
        return True
print('---------------------------------')
print('NDFA2 test')
print('aaaa',NDFA2('aaaa'))
print('bbbb',NDFA2('bbbb'))
print('abbb',NDFA2('abbb'))
print('baaa',NDFA2('baaa'))   
print('---------------------------------')
print('testing if string belongs to both NDFAs')
if(NDFA1('abb') == True and NDFA2('abb') == True):
    print('abb','acceptance')
else:
    print('abb','not accepted')


