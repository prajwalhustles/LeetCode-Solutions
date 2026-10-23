class Solution(object):
    def sortArray(self, nums):
        
        def merger(left,right):
            i,j=0,0
            result=[]
            n,m=len(left),len(right)
            while i<n and j<m :
                if left[i]<=right[j]:
                    result.append(left[i])
                    i+=1
                else:
                    result.append(right[j])
                    j+=1
            while(i<n):
                result.append(left[i])
                i+=1
            while(j<m):
                result.append(right[j])
                j+=1
            return result
        def merge(nums):
            if len(nums)<=1:
                return nums
            mid=len(nums)//2
            left_arr=nums[:mid]
            right_arr=nums[mid:]
            left=merge(left_arr)
            right=merge(right_arr)
            return merger(left,right)
        return merge(nums)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna