class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        string=str(x)
        i=0
        j=len(string)-1
        while i<j:
            if string[i]!=string[j]:
                return False
            i+=1
            j-=1
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna