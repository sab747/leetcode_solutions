class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        if not s or not wordDict:
            return False
        d = set(wordDict)
        
        dp = [0 for x in range(len(s))]
        
        for i in range(len(s)):
            print(s[:i+1])
            if s[:i+1] in d:
                dp[i] = 1
            else:
                for j in range(1,i+1):
                    print(s[j:i+1])
                    if s[j:i+1] in d and dp[j-1] == 1:
                        dp[i] = 1
                        break
                        
        return dp[-1]
                    
