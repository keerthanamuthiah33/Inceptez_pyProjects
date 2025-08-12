"""String Slicing
[start:stop:step]
"""

orgname="Inceptez"
print("Index 0:",orgname[0])
print("Index 1:",orgname[1])
print("Index 2:",orgname[2])
print("Index 3:",orgname[3])
print("Index 4:",orgname[4])
print("Index 5:",orgname[5])
print("Index 6:",orgname[6])
print("Index 7:",orgname[7])

"""
0 1 2 3 4 5 6 7 --> Positive Index
i n c e p t e z 
-8 -7 -6 -5 -4 -3 -2 -1 --> Negative Index
"""
print("Last Character:",orgname[-1])
print("First Character:",orgname[0])
n=len(orgname)
print("length of the string",n)
print("Extract first 4 character usint positive index",orgname[0:4])
print("Extract first 4 character usint negative index",orgname[-8:-4])
print("Extract first 4 character usint positive index",orgname[:4])
print("Extract first 4 character usint negative index",orgname[4:])
print("Extract first 4 character usint negative index",orgname[4:n])

print("first index to remaining:",orgname[1:n])

"skipping characters"
print("skipping characters:",orgname[0::2])

#reverse yhe string

print("does not reverse characters:",orgname[:]) #Does not reverser just prints the characters
print("reverse characters:",orgname[::])  #Does not reverser just prints the characters
print("reverse characters:",orgname[::1])  #Does not reverser just prints the characters
print("reverse characters:",orgname[::-1]) #--Reverses from back to front


#returns the first occurance of the word as index value
str1="Messi is the best soccer player"
str2=str1.find("soccer") #if i give cricket the index will be -1
print(str2)

print("soccer"in str1) # prints boolean value True

#Replace with Variables

l1="q"
l2="w"
l3="e"
l4="r"

#end= --check wthat is this
print("Spark supports lan like q,w,e,r")
print("Spark supports lan like",l1,",",l2,",",l3,",",l4)
print("Spark supports lan like " +l1+","+l2+","+l3+","+l4+"")
r1="r1:spark supports lan like {},{},{},{}".format(l1,l2,l3,l4)
print(r1)
r2="r2:spark supports lan like {0},{2},{1},{3}".format(l1,l2,l3,l4)
print(r2)
print(f"spark supports lan like {l1},{l2},{l3},{l4}") #f is called as string formarter it means we are gng to use variables inside a string
r3=f"r3:spark supports lan like {l1},{l2},{l3},{l4}"
print(r3)

#if f is not used the calculation will not happen
#only if F is used the actual calculation will happen
a=10
b=20
c=a+b
print(f"sum of {a}+{b}={a+b}")
print(f"sum of {a}+{b}={c}")
print("sum of {a}+{b}={c}")

#Multi line strings#

s1='''Py is a easy lan.
      it supports mul prog paradigm.
    its an interesting lan.'''
print(s1)

#string is mutable/immutable
#in python string is immutable (not changable once datatype is assigned)
s1="Inceptez"
print(type(s1))
print(id(s1))
s1="Azure DataBricks"
print(id(s1))
print(s1[0])
#s1[0]="Z"--does not allow edit or change the data thats inside 
