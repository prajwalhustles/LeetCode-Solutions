class Solution:
    def backspaceCompare(self, s, t):
        def clear(val):
            res=""
            for i in range(len(val)):
                if val[i]=="#":
                    res = res[:-1]

                else:
                    res+=val[i]
            
            return res

        return clear(s) == clear(t)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna