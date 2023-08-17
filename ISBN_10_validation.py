#Kata link : https://www.codewars.com/kata/51fc12de24a9d8cb0e000001/python
'''
ISBN-10 identifiers are ten digits long. The first nine characters are digits 0-9. 
The last digit can be 0-9 or X, to indicate a value of 10.
An ISBN-10 number is valid if the sum of the digits multiplied by their position modulo 11 equals zero.

EXAMPLE
ISBN     : 1 1 1 2 2 2 3 3 3  9
position : 1 2 3 4 5 6 7 8 9 10

This is a valid ISBN, because:
(1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0

1112223339   -->  true
111222333    -->  false
1112223339X  -->  false
1234554321   -->  true
1234512345   -->  false
048665088X   -->  true
X123456788   -->  false
'''
def valid_ISBN10(isbn):
    
# Method 1   
    # try:
    #     add = 0
    #     for i,num in enumerate(str(isbn), start=1):
    #         if num == 'X':
    #             num = 10
    #         add = add + (i*int(num))
    #     return True if add % 11 == 0 and len(str(isbn)) == 10 and 'X' not in isbn[:-1] else False 
    # except :
    #     return False  

# Simple Method
    try :
        return True if sum([i*int(num) if num != 'X' else i * 10 for i,num in enumerate(str(isbn), start=1)]) % 11 == 0 and len(str(isbn)) == 10 and 'X' not in isbn[:-1] else False
    except :
        return False

print("1. 1112223339 = ",valid_ISBN10('1112223339'))
print("2. 048665088X = ",valid_ISBN10('048665088X'))
print("3. 1293000000 = ",valid_ISBN10('1293000000'))
print("4. 1234554321 = ",valid_ISBN10('1234554321'))
print("5. 1234512345 = ",valid_ISBN10('1234512345'))
print("6. 1293 = ",valid_ISBN10('1293'))
print("7. X123456788 = ",valid_ISBN10('X123456788'))
print("8. ABCDEFGHIJ = ",valid_ISBN10('ABCDEFGHIJ'))
print("9. XXXXXXXXXX = ",valid_ISBN10('XXXXXXXXXX'))
print("10.123456789T = ",valid_ISBN10('123456789T'))