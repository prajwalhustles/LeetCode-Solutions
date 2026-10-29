class Solution:
    def sortedSquares(self, nums):
        i=0
        res=[]
        j=len(nums)-1
        while i<=j:
            if nums[i]**2<nums[j]**2:
                res.append(nums[j]**2)
                j-=1
            else:
                res.append(nums[i]**2)
                i+=1
        res=res[::-1]
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna