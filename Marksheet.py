import random   
rn=random.randint(1700000,1800000)
name=input("ENTER YOUR FULL NAME : ")
seat=input("ENTER YOUR SEAT NUMBER : ")
line=('_'*165)
g_v=0
g_vl=0
class Marksheet:
     def __init__(self,ext,inr,credit):
          self.ext=ext
          self.inr=inr
          self.total=ext+inr
          self.credit=credit
     
     def GP(self):
          if (self.inr<8 or self.ext<32):         return '--'
          elif (self.total>=80):    return 10
          elif (self.total>=75):    return 9
          elif (self.total>=70):    return 8
          elif (self.total>=60):    return 7
          elif (self.total>=50):    return 6
          elif (self.total>=45):    return 5
          elif (self.total>=40):    return 4
          else:  return '--'
     
     def GP_lab(self):
          if (self.inr<10 or self.ext<10):   return '--'
          elif(self.total>=40):             return 10
          elif (self.total>=38):            return 9
          elif (self.total>=35):            return 8
          elif (self.total>=30):            return 7
          elif (self.total>=20):            return 6
          else:  return '--'



     def CGP(self):                                    #Credit * GradePoint
          cgp=self.GP()
          if (type(cgp)==str):
               return '--'
          elif (cgp>0):
               return (self.credit)*cgp
     
     def CGP_lab(self):
          cgp=self.GP_lab()
          if (type(cgp)==str):
               return '--'
          else:
               return (self.credit)*cgp                     

     def CE(self):                                    #calculating of Credit Earn
          global g_v
          ce=self.CGP()
          if(type(ce)==str):
               g_v=1
               return '--'
          else:
               return self.credit

     def CE_lab(self):
          #global g_vl=1
          ce=self.CGP_lab()
          if(type(ce)==str):
               g_vl=1
               return '--'
          else:
               return self.credit


          
def sum(a,b,c,d,e,f,g,h,i):                                         #function for addition
     list=[a,b,c,d,e,f,g,h,i]
     sum=0
     for i in range(0,9):
          if(type(list[i])==int):
               sum=sum+list[i]
     return sum

def swapcase(oldStr):                                  #swaping string in upperCase
    newStr = ""
    for s in oldStr:
        if s.islower():
            newStr+=s.upper()
        elif s.isupper():
            newStr+=s
        else:
            newStr+=s
    return newStr

def pointer(b,c):                                      #calculating pointer
     if(g_v==0 and g_vl==0):
          f=c/b
          g=float("{0:.2f}".format(f))
          return g
     else:
          return '--'

def remark(pointer):                                   #Remark
     if(type(pointer)==str):
          return 'UNSUCCESSFUL'
     else:
          return 'SUCCESSFUL'

def grade(marks,outof):
     perc=(marks/outof)*100
     if(perc>=80):      return 'O'
     elif(perc>=75):     return 'A'
     elif(perc>=70):     return 'B'
     elif(perc>=60):     return 'C'
     elif(perc>=50):     return 'D'
     elif(perc>=45):     return 'E'
     elif(perc>=40):     return 'P'
     else:           return 'F'

def OAgrade(marksIn,marksExt,outof):
     perc=((marksIn+marksExt)/outof)*100
     if(perc>=80):      return 'O'
     elif(perc>=75):     return 'A'
     elif(perc>=70):     return 'B'
     elif(perc>=60):     return 'C'
     elif(perc>=50):     return 'D'
     elif(perc>=45):     return 'E'
     elif(perc>=40):     return 'P'
     else:             return '--'

arr=['M3','DLDA','DIS','ECCF','DS']
inr,ext=[],[]
for i in range(0,5):
     p=int(input("Enter External marks of {} out of 80 : ".format(arr[i])))                #taking input(internal marks) from user
     ext.append(p)
     q=int(input("Enter Internal marks of {} out of 20 : ".format(arr[i])))               #taking input(external marks) from user
     inr.append(q)
M3=Marksheet(ext[0],inr[0],5)                                            #creating object of class Marksheet
DLDA=Marksheet(ext[1],inr[1],4)
DIS=Marksheet(ext[2],inr[2],4)
ECCF=Marksheet(ext[3],inr[3],4)
DS=Marksheet(ext[4],inr[4],4) 

dldaprac=int(input("Enter practical marks of DLDA lab: "))                        #taking practical & tw marks from user
dldatw=int(input("Enter TermWork marks of DLDA lab: "))
dlda=Marksheet(dldaprac,dldatw,1)   

eccfprac=int(input("Enter practical marks of ECCF lab: "))
eccftw=int(input("Enter TermWork marks of ECCF lab: "))
eccf=Marksheet(eccfprac,eccftw,1)   

dsprac=int(input("Enter practical marks of DS lab: "))
dstw=int(input("Enter TermWork marks of DS lab: "))
ds=Marksheet(dsprac,dstw,1)

oopmprac=int(input("Enter practical marks of OOPM lab: "))
oopmtw=int(input("Enter TermWork marks of OOPM lab: "))
oopm=Marksheet(oopmprac//2,oopmtw//2,2)   
print("*"*165)
print("\t\t\t\t\t\t\t\t       UNIVERSITY OF MUMBAI\n")
print("\t\t\t\t\t\t\t\t\tANJUMAN-I-ISLAM'S")
print("\t\t\t\t\t\t\t\tKALSEKAR TECHNICAL CAMPUS, NEW PANVEL")
print("\t\t\t\t\t\t\t\t SCHOOL OF ENGINEERING & TECHNOLOGY")
print(line)
print(" NAME          : {}".format(swapcase(name)))
print(" EXAMINATION   : SECOND YEAR ENG. (SEMESTER III) CBCGS")
print(" BRANCH        : COMPUTER ENGINEERING")
print(" HELD IN       : DECEMBER 2017 (REGULAR)")
print(" SEAT NUMBER   : {}\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  REGISTRATION NO : {}".format(swapcase(seat),rn))
print(line)
print(" COURSE\t\tCOURSE TITLE  \t\t\t COURSE\t\t\t\t***GRADE***      \t\t CREDIT\t\t  GRADE\t  ")
print("  CODE \t\t  \t\t\t\t CREDIT\t\t  PR/OR\t\t  IA/TW\t\t OVERALL\t  EARND\t\t  POINT\t\t   C*GP")
print(line)
print(" CSC301  APPLIED MATHEMATICS-3\t\t\t   {}\t\t    {}\t\t    {}\t\t    {}\t\t    {}\t\t    {}\t\t    {}".format(M3.credit,grade(M3.ext,80),grade(M3.inr,20),OAgrade(M3.inr,M3.ext,100),M3.CE(),M3.GP(),M3.CGP()))
print(line)
print(" CSC302  DIGITAL LOGIC DESIGN & ANALYSIS\t   {}\t\t    {}\t\t    {}\t\t    {}\t\t    {}\t\t    {}\t\t    {}".format(DLDA.credit,grade(DLDA.ext,80),grade(DLDA.inr,20),OAgrade(DLDA.inr,DLDA.ext,100),DLDA.CE(),DLDA.GP(),DLDA.CGP()))
print(line)
print(" CSC303  DISCRETE STRUCTURE\t\t\t   {}   \t\t    {}\t\t    {}\t\t    {}\t\t    {}\t\t    {}\t\t    {}".format(DIS.credit,grade(DIS.ext,80),grade(DIS.inr,20),OAgrade(DIS.inr,DIS.ext,100),DIS.CE(),DIS.GP(),DIS.CGP()))
print(line)
print(" CSC304  ELEC. CIRCUIT & COMM. FUNDAMENTALS\t   {}\t\t    {}\t\t    {}\t\t    {}\t\t    {}\t\t    {}\t\t    {}".format(ECCF.credit,grade(ECCF.ext,80),grade(ECCF.inr,20),OAgrade(ECCF.inr,ECCF.ext,100),ECCF.CE(),ECCF.GP(),ECCF.CGP()))
print(line)
print(" CSC305  DATA STRUCTURE\t\t\t\t   {}\t\t    {}\t\t    {}\t\t    {}\t\t    {}\t\t    {}\t\t    {}".format(DS.credit,grade(DS.ext,80),grade(DS.inr,20),OAgrade(DS.inr,DS.ext,100),DS.CE(),DS.GP(),DS.CGP()))
print(line)
print(" CSE301  DIGITAL SYSTEM LAB\t\t\t   {}\t\t    {}\t\t    {}\t\t    {}\t\t    {}\t\t    {}\t\t    {}".format(dlda.credit,grade(dlda.ext,25),grade(dlda.inr,25),OAgrade(dlda.inr,dlda.ext,50),dlda.CE_lab(),dlda.GP_lab(),dlda.CGP_lab()))
print(line)
print(" CSE302  BASIC ELECTRONICS LAB\t\t\t   {}\t\t    {}\t\t    {}\t\t    {}\t\t    {}\t\t    {}\t\t    {}".format(eccf.credit,grade(eccf.ext,25),grade(eccf.inr,25),OAgrade(eccf.inr,eccf.ext,50),eccf.CE_lab(),eccf.GP_lab(),eccf.CGP_lab()))
print(line)
print(" CSE303  DATA STRUCTURE LAB\t\t\t   {}\t\t    {}\t\t    {}\t\t    {}\t\t    {}\t\t    {}\t\t    {}".format(ds.credit,grade(ds.ext,25),grade(ds.inr,25),OAgrade(ds.inr,ds.ext,50),ds.CE_lab(),ds.GP_lab(),ds.CGP_lab()))
print(line)
print(" CSE304  OOPM (JAVA) LAB    \t\t\t   {}\t\t    {}\t\t    {}\t\t    {}\t\t    {}\t\t    {}\t\t    {}".format(oopm.credit,grade(oopmprac,50),grade(oopmtw,50),OAgrade(oopmprac,oopmtw,100),oopm.CE_lab(),oopm.GP_lab(),oopm.CGP_lab()))
print('\n\n\n\n\n')

print(line)
a=(M3.credit+DLDA.credit+DIS.credit+ECCF.credit+DS.credit+dlda.credit+eccf.credit+ds.credit+oopm.credit)
b=sum(M3.CE(),DLDA.CE(),DIS.CE(),ECCF.CE(),DS.CE(),dlda.CE_lab(),eccf.CE_lab(),ds.CE_lab(),oopm.CE_lab())
c=sum(M3.CGP(),DLDA.CGP(),DIS.CGP(),ECCF.CGP(),DS.CGP(),dlda.CGP_lab(),eccf.CGP_lab(),ds.CGP_lab(),oopm.CGP_lab())

print("\t\t\tTOTAL\t\t\t   {}\t\t\t\t\t\t\t\t    {} \t\t    --\t\t    {}".format(a,b,c))
print(line)
point=pointer(b,c)
print("\n REMARK :  {}\t\t\t\t\t\t\tSGPI : {}\t\t\t\t\t CGPI : -- ".format(remark(point),point))
print("*"*165)



