from multiprocessing.sharedctypes import Value


d = {'name':["Nitya","Nitu"],"followers":174,"online":True,345:{"age":45}}
"""
keys : name,followers,online,345

values:Nitya,174,True,id

"""
for i in d.keys():
    print(d[i])
print(d)
print(type(d))   
print(type(d.keys())) 

print(d["online"])
print(d[345])
print(d.values())
print(type(d["name"]))
print(d[345]["age"])

d['Sports']='football'
print(d)

print(d['name'][1][1:4])

# updating in dictionary
d.update({'hobby':'paintaing'})
print(d)

# deleting in dictionary
del d['name'][0]
print(d)

d.clear()
print(d)

