'''
Complete the function/method so that it takes a PascalCase string and returns 
the string in snake_case notation. Lowercase characters can be numbers. 
If the method gets a number as input, it should return a string.

Examples 
"TestController"  -->  "test_controller"
"MoviesAndBooks"  -->  "movies_and_books"
"App7Test"        -->  "app7_test"
1                 -->  "1"
'''

import re

def to_underscore(string):
    # your code here
    index = []

    if type(string).__name__ != 'int':

        for i,char in enumerate(string) :
            if i != 0 and char.isupper():
                index.append(i)
        increase = 0
        for x in index : 
            string = string[:x+increase] + "_" + string[x+increase:]
            increase += 1

        string = re.sub(r'__', '_', string)    

    return str(string).lower()
    pass

print(to_underscore('TestController'))
print(to_underscore('MoviesAndBooks'))
print(to_underscore('Movies_And_Game'))  
print(to_underscore('App7Test')) 
print(to_underscore(1))     