class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S:
            return None
        
        last = {}
        for i in range(len(S)):
            last[S[i]] = i
            
        partitions = []
        anchor = 0
        j = 0
        for i in range(len(S)):
            j = max(last[S[i]],j)
            if i == j:
                partitions.append(j-anchor+1)
                anchor = i+1
                
                
            
        return partitions
        
