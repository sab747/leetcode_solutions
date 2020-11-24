"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
​
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if not head:
            return None
        
        curr = head
        node_dict = {}
        index = 0
        while curr:
            node_dict[curr] = Node(curr.val)
            curr = curr.next
            index += 1
        
        index = 0
        curr = head
        print(head.val)
        while curr:
            print(curr.val)
            r = curr.random
            n = curr.next
            if r:
                node_dict[curr].random = node_dict[r]
            else:
                node_dict[curr].random = None
            if n:
                node_dict[curr].next = node_dict[n]
            else:
                node_dict[curr].next = None
            index += 1
            curr = curr.next
            
        return node_dict[head]
            
            
        
