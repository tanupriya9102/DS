# NEXT GREATER ELEMENT TO RIGHT
arr=[1,3,2,4]
s=[]
v=[]



for i in reversed(range(len(arr))):
    if len(s)==0:
        v.append(-1)
        s.append(arr[i])
    else:
        if(arr[i]<s[0]):
            v.append(s[0])
            s.append(arr[i])
        else:
            while(arr[i]>=s[0]):
                s.pop()
            v.append(s[0])
            s.append(arr[i])

print(s)
print(v)
            
                
            
            
        
    
