class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        
        bigR = [0 for x in range(n)]
        bigL = [0 for x in range(n)]
        
        for i in range(1, n):
            bigR[n-i-1] = max(bigR[n-i],height[n-i])
            bigL[i] = max(bigL[i-1],height[i-1])
          
        total = 0
        for i in range(n):
            if min(bigR[i],bigL[i]) > height[i]:
                total += min(bigR[i],bigL[i]) - height[i]
            
        return total
