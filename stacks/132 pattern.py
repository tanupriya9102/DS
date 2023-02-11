import sys
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        st=[]
        x=-sys.maxsize - 1
        for i in reversed(range(len(nums))):
            if nums[i]<x:
                return True
            while(len(st)!=0 and st[-1]<nums[i]):
                x=st[-1]
                st.pop()
            
            st.append(nums[i])
        return False
