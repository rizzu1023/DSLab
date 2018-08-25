def f(a,b):
	c=[]
	if a>=b:
		c.append(1)
		##d=a[3:7]^b+a[2]
	else:
		c.append(0)
		##d=a[3:7]+a[2]
	print(a,b,c)
##def a():

a=[]
b=[]
for i in range(4):
	x=int(input())
	a.append(x)
for i in range(3):
	a.append(0)

for i in range(4):
	x=int(input())
	b.append(x)

##print(a)
##print(b)
f(a,b)
