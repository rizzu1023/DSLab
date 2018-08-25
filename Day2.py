
# coding: utf-8

### DICTIONARY

# In[27]:

#my first programme
print("Hello world")


# In[5]:

dict={}  #to initialize empty dictionary
eg. student = {'key'=value}   #key will not change but value


# In[7]:

student={'name':'John','rollno':15}
print(student)


# In[10]:

student.get('name')                                                                #get function


# In[11]:

print(student.get('phone'))


# In[12]:

print(student.get('phone','not found'))


# In[13]:

student['phone']=8441988897


# In[14]:

student


# In[28]:

Marks={'DIS':18,'DLDA':18,'ECCF':11,'DS':10}
Marks.get('DIS'),Marks.get('ECCF'),Marks.get('AM')


# In[33]:

Marks={'DIS':18,'DLDA':18,'ECCF':11,'DS':10}                  #updation
student.update(Marks)
student


# In[34]:

del student['name']                            #delete keyword for deleting a specific value from dictionary
student


# In[36]:

b=student.pop('rollno')                                          #pop function
b


# In[38]:

len(student)                                            #for finding length of dictionary


# In[39]:

student.keys()


# In[40]:

student.values()


# In[43]:

list(student.keys())


# In[47]:

month={1:'January',2:'Fabruary',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
month.get(5)


# In[55]:

a=34                                                                   #if condition
if(a==34):
    print("TRUE")


# In[56]:

a=19
if(a==12):                                                              #else codition
    print('TRUE')
else:
    print('False')


# In[59]:

a=12
if(a==32):
    print('false')                                                  #if else
elif(a==23):
    print('True')
else:
    print('FALSE')


# In[61]:

a=13
b=1
if(a==13):
    if(b==1):
        print("Hello")
        print("you are in nested if")


# In[62]:

x=int(input("Enter a Number"))                                    #odd even programme
if(x%2==0):
    print("Given number is Even")
else:
    print("Given number is odd")


# In[67]:

words=['First','Second']                                                    #for loop
for i in words:
   print(i)
            


# In[68]:

words=['hello','world','any',10]                                          #for loop

for i in range(1,len(words)):
    print(words[i])
    


# In[71]:

str='Rizwan'                                                     #for loop

for i in range(0,2,):
    print(str)


# In[73]:

n=int(input())

for i in range(1,n+1,):
    print(i)


# In[77]:

n=int(input())                                      #sum using for loop
sum=0
for i in range(0,n+1):
    sum+=i
print(sum)


# In[87]:

n=int(input())                                         #factorial using for loop
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)


# In[89]:

i=0                                                       #while loop
while(i<10):
    i+=1
print('out of while')


# In[1]:

n=int(input())                                #armstrong number
c,a=0,0
temp=n
print(temp)
while n>0:
    a-n%10
    c+=(a*a*a)
    n=n//10
if temp==c:
        print("it is an armstrong number")
else:
        print("it is not an armstrong number")
        


## FUNCTIONS

# In[2]:

def foo():                                                             #function
    print('i am in foo')

foo()


# In[51]:




# In[6]:

def add():                                                          #return function
    c=10+20
    return c
add()


# In[8]:

def add(a,b):                                                            #funtion call by value
    c=a+b
    return c
d=24
e=43
c=add(d,e)
print(c)


# In[10]:

def add(d,e):                                             
    c=d+e
    return c
d=10
e=34
c=add(d=10,e=34)                                               #keyword argument
c-20


# In[11]:

def evenodd(a):                                                 #odd even using function
    if(a%2==0):
        print("given no is even")
    else:
        print("given no is odd")

x=int(input("Enter a number"))
evenodd(x)


# In[15]:

def sqr(x):
    list=[]
    for i in range(x+1):
        sq=i**2
        list.append(sq)
    return list
sqr(10)


# In[17]:

def hoo():                                                 #calling a function inside a function
    print("i am in hoo")
def foo():
    print("i am in foo")
    hoo()
foo()


### FILE

# In[18]:

#r  ->  react
#w  ->  write
#r+ ->  read and write
#a  ->  append


# In[19]:

f=open('text.txt','w')                                          #file syntax


# In[20]:

f.write("hiee i am javed gouri")                                 #open and write in file


# In[21]:

f.close()                                                        #close file


# In[23]:

f=open('text.txt','w')
f.write('1)Hussain')
f.write('2)Juber')
f.write('3)Atay')


# In[24]:

f.close()


# In[26]:

with open('text.txt','w') as f:                                  #open a file 
    f.write('1)zaid')                                            #it will be automatically close the file


# In[27]:

with open('text.txt','a') as f:
    f.write('5)abdul kadir')


# In[28]:

with open('text.txt','r') as f:                                  #reading a file and print it's content
    filecontent=f.read()
print(filecontent)


# In[33]:

with open('text.txt','r') as f:
    filecontent=f.readlines()                                     #readlines concept
print(filecontent)


# In[34]:

with open('text.txt','r') as f:
    filecontent=f.readline()                                     #readline concept
print(filecontent)


# In[42]:

with open('text.txt','r') as f:
    filecontent=f.read(25)
print(filecontent)


# In[45]:

a=[1,2,4,5]
for i in a:
    print(i,end='# ')


# In[49]:

with open('text.txt') as rf:                                #by default it will be in read mode
      with open('test_copy','w') as wf: 
        for line in rf:                                     #copying a file into another file
            wf.write(line)


# In[50]:

0/0


# In[51]:

a=b


# In[56]:

try:
    a=b
except Exception:                                  #Exception is use for axcepting all type error
    print("Something went wrong")


# In[63]:

try:                                                        #with specific error
    f=open('test.txt')
except FileNotFoundError:
    print('Sorry the file doesnt exist')
else:
    a=f.read()
    print(a)


# In[64]:

try:                                
    f=open('text.txt')
except FileNotFoundError:
    print('Sorry the file doesnt exist')
else:
    a=f.read()
    print(a)


# In[70]:

x=[i**2 for i in range(20)]                                 #python ka jhol       #comprihencive list
x


# In[80]:

x=[i for i in range(20) if i%2==0]                            #python ka dusra jhol
x                                                             #even number


# In[ ]:



