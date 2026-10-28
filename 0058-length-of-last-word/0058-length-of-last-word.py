class Solution:
    def lengthOfLastWord(self, s):
        res=0
        for i in range(len(s)-1,-1,-1):
            if s[i].isalpha():
                res+=1
            elif res>0:
                break
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna