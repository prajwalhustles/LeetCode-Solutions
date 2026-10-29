class Solution(object):
    def moveZeroes(self, nums):
        j=0
        i=0
        while i<len(nums):
            if nums[i]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
            i+=1
        return nums
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna