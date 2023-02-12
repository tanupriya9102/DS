# using stack nearest smaller to left and nearest smaller to right
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if(len(heights)==1):
            return(1*heights[0])
        left=[]
        right=[]
        st=[]
        area=[]
        left.append(-1)
        st.append(0)
        # nearest smaller to left
        for i in range(1,len(heights)):
            while(len(st)!=0 and heights[i]<=heights[st[-1]]):
                st.pop()
            if(len(st)==0):
                left.append(-1)
                st.append(i)
            else:
                left.append(st[-1])
                st.append(i)
        st.clear()
        right.append(len(heights))
        st.append(len(heights)-1)

        # nearest smaller to right
        for i in reversed(range(len(heights))):
            while(len(st)!=0 and heights[i]<=heights[st[-1]]):
                st.pop()
            if(len(st)==0):
                right.append(len(heights))
                st.append(i)
            else:
                right.append(st[-1])
                st.append(i)
        right[:]=right[::-1]
        for i in range(len(heights)):
            area.append((right[i]-left[i]-1)*heights[i])
        return(max(area))

            

            

        
            
