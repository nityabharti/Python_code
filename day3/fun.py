from itertools import count


def length(ls):
    count=0
    for i in ls:
        count=count+1
    return count

def minimum(ls):
    mini=1000
    for i in ls:
        if mini>i:
            mini=i
    return mini 


    


ls=[34,56,75,29,30,43,45,24,31,26,38,87,99]


for i in range(length(ls)):
    print(ls[i])
ls.sort()
print(ls)   

ls1=[20,10,90,60,300,400,288,76,45,38,29,9,30]
print(length(ls1))
ls2=[1,2,65,76,87,47,45,28,29,"number"]
print(length(ls2))
print(minimum(ls))
print(minimum(ls1))

sum=0
for i in ls:
    sum+=i
print(sum)  

# def power(value1,value2):
#     return value1**value2
print(pow(2,4))    


