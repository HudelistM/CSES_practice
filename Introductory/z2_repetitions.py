#Moj pokušaj
#dna=[str(x) for x in input()]
#counter=[]
#for i in range(len(dna)):
#    counter.append(dna.count(dna[i]))
#print(counter)
#print(max(counter))
#----------------------------
#Dobro rešenje
lst=list(input())
count=1
maxx=1
for i in range(1,len(lst)):
    if lst[i]==lst[i-1]:
        count+=1
    else:
        count=1
    if count>maxx:
        maxx=count
print(maxx)

