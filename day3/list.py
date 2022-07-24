# ls =["Nitya","Neha","Akansha",""   ]

# ls = ["name",True,68.99,23]
# print(ls)
# print(type(ls))  #list

# ls=["name",["place",70],True]
# print(ls)

"""
ls =["Nitya","Neha","Akansha","Ambuj","Divya","Piyush","Ayush"   ]
        0       1       2        3       4       5        6            
       -7      -6      -5        -4      -3     -2       -1
"""
# ls =["Nitya","Neha",89.9,"Akansha","Ambuj",92.99,"Divya",True,"Piyush",69,"Ayush"]
# print(ls[4])
# print(ls[-3])
# print(ls[7])
# print(ls[-4])
# print(ls[5],ls[-2])

# ls[3]="Akanshu"
# print(ls)
# ls[-4]="Nitu"
# print(ls)

# ls.sort()
# print(ls)

ls=[87,59,38,36,76,27,87,40,37,20,19]
print(max(ls))
ls.sort()
print(ls)
ls.reverse()
print(ls)
ls.pop()
print(ls)

# for i in range(len(ls)):
   
#     ls.sort()
#     print(ls[i])

maximum=-1
for i in ls:
    if maximum<i:
        maximum=i
print(maximum)          
    

# ls.insert(2,"Cheetah")
# print(ls)
# del(ls[2])
# print(ls)

# print(ls[3:8])#list slicing
# print(ls[3: ])
# print(ls[9: ])
# print(ls[:])

# list1 = ['physics', 'chemistry', 1997, 2000]
# list2 = [1, 2, 3, 4, 5, 6, 7 ]
# print ("list1[0]: ", list1[0])  #list slicing
# print ("list2[1:5]: ", list2[1:5])