## add and reverse


N=int(input())
A=[]
for i in range(N):
    x= input()
    y=int(x)
    A.append(y)
print(A)
B=[]
C=[]
i=N-1
k=0
while i >= 0:
    temp1= A[i]
    B.append(temp1)
    temp2= A[k]+B[k]
    C.append(temp2)
    i= i-1
    k=k+1
print(B)
print(C)
