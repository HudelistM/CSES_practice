n=int(input())
MOD=1000000007
answer=1
for i in range(n):
    answer*=2
    answer%=MOD
print (answer)