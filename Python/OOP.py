class Student:
     
	def __init__(self,first,last,CGPI,mobile):
		self.first=first
		self.last=last
		self.CGPI=CGPI
		self.email=last+'.'+'@gmail.com'
		self.mobile=mobile
	
	def perc(self):
		if (self.CGPI<7):     return (self.CGPI*7.1)+12
		   
		else:    return (self.CGPI*7.4)+12
			
		
	def fullname(self):
           a=self.perc()
           print(a)
   		 #return '{} {}'.format(self.first,self.last)
	 
		
n=input("enter")
	
std1=Student(n,'Rizwan',7.42,8441988897)





print(std1.perc())
print(std1.fullname())
print(std1.CGPI)
