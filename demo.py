# ham tinh luy thua tu nhien
def exp(a, n):
    p=1
    for i in range(n):
        print("i=",i,"p*a=",p,"*",a,"=",p*a)
        p=p*a
    return p
exp(2,8)
#ham tinh luy thua chia de tri
def exp(a, n):
       if n==0:
           print("exp(",a,",",n,")=")
           print(1)
           return 1 
       else:
           b=exp(a, n//2)
           print("exp(",a,",",n,")=")
           if n%2==0:
               print(b*b)
               return b*b 
           else:
               print(a*b*b)
               return a*b*b 
#exp(2,9)        
# thuat toan tim kiem tuan tu
def valueClosest(A,K):
        n=len(A)
        if K<=A[0]:
             return A[0]
        elif K>=A[n-1]:
             return A[n-1]
        else:
             value=A[0]
             for i in range(n):
                print("i=",i,"value=",value)
                if abs(A[i]-K)<abs(value-K):
                     value=A[i]
        return value
#A = [2,5,8,11,13,14,17,20]
#K = 15
#valueClosest(A,K)
#thuat toan tim kiem nhi phan
def valueClosest1(A,left,right,K):
          print("valueCloset1(A",left,right,K,")")
          if left==right:
               return A[left]
          elif left==right-1:
               if abs(A[left]-K)<abs(A[right]-K):
                    return A[left]
               else:
                    return A[right]
          else:
             mid=(left+right)//2
             if A[mid]==K:
                  return A[mid]
             elif K<A[mid]:
                  return valueClosest1(A,left,mid,K)
             else:
                  return valueClosest1(A,mid,right,K)
A = [2,5,8,11,13,14,17,20]
K = 15
valueClosest1(A,0,len(A)-1,K)        


