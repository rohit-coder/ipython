#Lambda or anonymous functions
def add(a,b):
	return a+b

#comaring lamda functions with def
#this is a one linear function based syntax
#minus = lambda a,b:a-b
#def minus(a,b):
#	return a-b	


#a = int(input("Enter a number"))
#b = int(input("Enter a number"))
#add(a,b)
#print(minus(a,b))

def a_first(a):
	return a[1]

a = [[2,6],[9,5],[12,9]]
a.sort(key=a_first)
print(a)

#using lamda

a = [[2,6],[9,5],[12,9]]
a.sort(key=lambda x:x[1])
print(a)
