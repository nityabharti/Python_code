# import random
from random import randint
"""
randiant(2,20)


"""

# k=randint(2,100)
# print(k)

nitya=["my","name","is","Nitya Bharti","i'm am from ","Bihar Darbhanga","i'm studying in", "central university of haryana"]
l=len(nitya)
k=randint(0,l-1)
print(nitya[k])

str=""
for i in nitya[k]:
    if(i==' ' or i=='a' or i=='o' or i=='e' or i=='i' or i=='u'):
         str+=i
         str+=" "
         continue

    str+="_ "
print(str)    