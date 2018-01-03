
'''
#My solution
import re

def checkio(data):
    
    if len(data) < 10 or len(data) > 64 or data.isupper() or data.islower() or data.isdigit():
       return False
    else:
        m_d = re.search('\d+',data)
        m_A = re.search('[A-Z]+',data)
        m_a = re.search('[a-z]+',data)
        return m_d != None and m_A!= None and m_a != None
'''

#best solution
checkio = lambda s: not(
        len(s) < 10
        or s.isdigit()
        or s.isalpha()
        or s.islower()
        or s.isupper()
    ) 
    


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
