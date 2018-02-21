#name=input("ENTER STUDENT'S NAME")
#seat=input("ENTER SEAT NUMBER")

class Marksheet:
     def __init__(self,inr,ex):
          self.inr=inr
          self.ex=ex
          self.total=inr+ex
     
     def GP(self):
          if (self.total>=80):     return 10
          elif (self.total>=75):    return 9
          elif (self.total>=70):    return 8
          elif (self.total>=60):    return 7
          elif (self.total>=50):    return 6
          elif (self.total>=45):    return 5
          elif (self.total>=40):    return 4
          else:  return '--'
 
     def CGP(self):
          cgp=self.GP()
          if (self.inr<8 or self.ex<32):
               return '--'
          elif (cgp>0):
               return 4*cgp
          else:
               return '--'
          
          
  
     
M3inr=int(input("Enter internal marks of M3: "))
M3ex=int(input("Enter external marks of M3: "))      
M3=Marksheet(M3inr,M3ex)



DLDAinr=int(input("Enter internal marks of DLDA: "))
DLDAex=int(input("Enter external marks of DLDA: "))      
DLDA=Marksheet(DLDAinr,DLDAex)


print("AM-3 \t {} \t {} \t 5 \t {} \t {}".format(M3.inr,M3.ex,M3.GP(),M3.CGP()))
print()
print("DLDA \t {} \t {} \t 4 \t {} \t {}".format(DLDA.inr,DLDA.ex,DLDA.GP(),DLDA.CGP()))

       

     
