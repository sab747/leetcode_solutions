class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        if len(points) < K:
            return points
        
        points = sorted(points, key=lambda x : sqrt(x[0]*x[0] + x[1]*x[1]))
        return points[:K]
