from telnetlib import PRAGMA_HEARTBEAT
from unicodedata import name


hi = "Hello "
duniya = 'world!!'
"""

    H   E    L    L    O
    0   1    2    3    4
    -5  -4  -3   -2   -1
"""
print(hi[2],hi[-4])

name=input("Enter your name: ")
print(hi,name)
# hi-= duniya
print(hi)
hi*=3
print(hi)
duniya='r'+duniya
print(duniya)

ls1=[1,2,3,4,5]
ls2=[6,7,8,9]
print(ls1+ls2)
print(ls1*3)

s="vulk thor man spider captain america black wido doctor stange ant man black panther winter summer rainy vision"
print(s[:])
print(s[10:])
print(s[:20])
print(s[20:30])
print(s.split())
print(s.count('a'))

# finding a string

string = 'Python Lovers'
print(string[7])
for i in range(len(string)):
    if string[i]=='L':
        print (i)
char ='t'
print(string.find(char))

char ='o'
print(string.find(char))
print(string.rfind(char))

char='s'
print(string.rfind(char))

s = "The Avengers"
print(s)
print(s.upper())
print(s.lower())
print(s.capitalize())

s1="er"
print(s1.zfill(7))
