def split(lists):
     A=lists[:3]
     Q=lists[4:]
     return A,Q

def shift(A,Q):
     Qn=Q[-1]
     res=A+Q
     e1=res[-1]
     for i,e2 in enumerate(res):
          res[i],e1=e1,e2
     A,Q=split(res)
     return A,Q,Qn

def listTostr(list1):
     str1 = ''.join(str(e) for e in list1)
     return str1

def strTolist(str1):
     c=list(str1)
     return c



def BinAdd(x,y):
        maxlen = max(len(x), len(y))

        #Normalize lengths
        x = x.zfill(maxlen)
        y = y.zfill(maxlen)

        result = ''
        carry = 0

        for i in range(maxlen-1, -1, -1):
            r = carry
            r += 1 if x[i] == '1' else 0
            r += 1 if y[i] == '1' else 0

            # r can be 0,1,2,3 (carry + x[i] + y[i])
            # and among these, for r==1 and r==3 you will have result bit = 1
            # for r==2 and r==3 you will have carry = 1

            result = ('1' if r % 2 == 1 else '0') + result
            carry = 0 if r < 2 else 1       

        if carry !=0 : result = '1' + result

        return result.zfill(maxlen)


def twoComp(list1):
     for i in range(len(list1)):        
          if(list1[i]==0):
               list1[i]=1
          elif(list1[i]==1):
               list1[i]=0
     l2=listTostr(list1)
     l=BinAdd(l2,'1')
     return l




def booth(A,Q,Qn,M):
     if(Q[-1]<Qn):
          print("A=A+M")
          a=listTostr(A)
          m=listTostr(M)
          
          A1=BinAdd(a,m)
          
          A=strTolist(A1)
          
          A,Q,Qn=shift(A,Q)
          return A,Q,Qn

     elif(Q[-1]>Qn):
          print("A=A-M")
          M=twoComp(M)
          a=listTostr(A)

          A1=BinAdd(a,M)

          A=strTolist(A1)

          A,Q,Qn=shift(A,Q)
          return A,Q,Qn

          
     elif(Q[-1]==Qn):
          print("Shifting")
          A,Q,Qn=shift(A,Q)
          return A,Q,Qn
          

          




def main():

     x=bin(int(input("Enter first Number")))
     y=bin(int(input("Enter Second Number")))

     q=list(x)
     q1=q[2::]
     m=list(y)
     m1=m[2::]
     m1=list(map(int,m1))
     q1=list(map(int,q1))


     a=[0,0,0,0]
     qn=0

     A,Q,Qn=booth(a,q1,qn,m1)
     A,Q,Qn=booth(A,Q,Qn,m1)
     A,Q,Qn=booth(A,Q,Qn,m1)
     A,Q,Qn=booth(A,Q,Qn,m1)

     res=A+Q
     print(res)

     print(q1,m1)

main()





          
          
              


          
