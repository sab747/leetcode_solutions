class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_length = 0
        curr = ""
        for i in range(len(s)):
            if s[i] not in curr:
                curr += s[i]
            else:
                if len(curr) > longest_length:
                    longest_length = len(curr)
                curr = curr.split(s[i])[1] + s[i]
                
        if len(curr) > longest_length:
            longest_length = len(curr)
        return longest_length
                
            
        
