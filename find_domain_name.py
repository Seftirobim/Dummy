
'''
link : https://www.codewars.com/kata/514a024011ea4fb54200004b/python

Write a function that when given a URL as a string, 
parses out just the domain name and returns it as a string. 

For example:
* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
'''
import re
def domain_name(url):
    resub = re.sub("^https:\/\/www.|^http:\/\/www.|^https:\/\/|^http:\/\/|w{3}.",'',url)
    enum = [i for i,char in enumerate(resub) if char == "/" or char == "."]
    return resub[:enum[0]] if len(enum) != 0 else resub

print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("https://www.cnet.com"))
print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("www.xakep.ru"))
print(domain_name("https://youtube.com"))
