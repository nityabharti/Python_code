print("Hello , World!")
x = 4
x = "Hello"
print(x)
_my_var =["RAM","SHYAM","SOHAN"]
x,y,z=_my_var
print(z,x,y)

def myfun():
    global x
    x="fantastic"
myfun() 
print("Python is " + x)  

b = "Bytecode Learners"
print(b.capitalize())
print(b.replace("B","H"))
print(b[:8])
print(b[9:])
print(b[2:9])
print(b[2:-9])

list = ["a","b","c","d"]
print(len(list))
list.insert(3,"z")
list.pop(0)
print(list)

tuple=("sa","re","ga","ma","pa","dha","ni","sa")
print(tuple)
print(len(tuple))

set={"1","2","3","4","5","6"}
print(set)

dict={
    "brand":"apple",
    "model":"macbook",
    "year":"2022",
}
p=dict.values()
print(p)


