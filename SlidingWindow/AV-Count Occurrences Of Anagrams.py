#Aditya Verma PL
from collections import Counter
s1="abc"
s2="abcbbacabb"
c1=Counter(s1)
k=len(s1)
n=len(s2)
l=[]
i=0
j=0
while(j<n):
    if(j-i+1<k):
        j+=1
    elif(j-i+1==k):
        c2=Counter(s2[i:j+1])
        if(c1==c2):
            l.append(''.join(s2[i:j+1]))
        i+=1
        j+=1
print(l)
    
    
