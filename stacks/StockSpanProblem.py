# stock span problem
# using Next greater element to left
arr=[100,80,60,70,60,75,85]
stack=[]
temp=[]
count=1
for i in arr:
    if (len(stack)==0 or len(stack)!=0 and i<stack[-1]):
        temp.append(1)
        stack.append(i)

        
    else:
        while(len(stack)!=0 and i>stack[-1]):
            stack.pop()
            count+=1
        temp.append(count)
        stack.append(i)
            
        
print(temp)
    
