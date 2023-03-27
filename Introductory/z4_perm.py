#Moj pokušaj(menjam susjedne brojeve ako im je razlika veća od 1(KRIVO))
#n=int(input())
#l=[i+1 for i in range(n)]
#for j in range(n):
#    for i in range(1,len(l)):
#        if(l[i]-l[-1]):
#            temp=l[i]
#            l[i]=l[i-1]
#            l[i-1]=temp
#print(l)
#----------------------------------------------------------------
#Dobro rešenje
n=int(input())
if n==1:
    print('1')
elif n<=3:
    print("NO SOLUTION")
else:
    for i in range(2,n+1,2):
        print(i,end=" ")
    for i in range(1,n+1,2):
        print(i,end=" ")
