a=5
print(a)
user="Rares"
password="euacum44"
len(password)
print("*"*len(password))

l1=[1,2,"3",8.9,True]

c,d,*rest=l1

print(c)
print(d)
print(rest)

m1=[[1,2],[3.4,4.5],["5","6"]]

tuple=('a','b','c')

s1=set(tuple)
print(s1)
s1.remove('a')
print(s1)

s2={1,2,3}
s3=s1.union(s2)
print(s3)


dict={'l5':[1,2,3],'age':25,'magic':False}

list(dict.items())