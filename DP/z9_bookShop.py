#Moje rešenje
#n,x=map(int,input().split(" "))
#optimal=0
#page_num=0
#lista_knjiga=[int(x) for x in input().split(" ")]
#lista_stranica=[int(x) for x in input().split(" ")]
#for i in range(n):
#    for j in range(n):
#        if i==j:
#            continue
#        rez=lista_knjiga[i]+lista_knjiga[j]
#        if (rez<x and rez>optimal):
#            optimal=rez
#            page_num=lista_stranica[i]+lista_stranica[j]
#print(page_num)
#Dobro rešenje
n,x=map(int,input().split())
lista_knjiga=[int(x) for x in input().split(" ")]
lista_stranica=[int(x) for x in input().split(" ")]
dp=[[0]*(x+1) for i in range(n+1)]

for i in range(1,n+1):
    for j in range(x+1):
        dp[i][j]=dp[i-1][j]
        if j>=lista_knjiga[i-1]:
            dp[i][j]=max(dp[i][j],dp[i-1][j-lista_knjiga[i-1]]+lista_stranica[i-1])
print(dp[n][x])