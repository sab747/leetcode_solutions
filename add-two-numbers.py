# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        b = 0
        sum = 0
        while l1 != None or l2 != None:
            if not l2:
                sum += l1.val* 10**b
                l1 = l1.next
            elif not l1:
                sum += l2.val* 10**b
                l2 = l2.next
            else:
                sum += l1.val* 10**b
                sum += l2.val* 10**b
                l1 = l1.next
                l2 = l2.next
            b += 1
        head = ListNode()
        if sum == 0:
            return head
        curr = head
        print(sum)
        while sum != 0:
            i = sum % 10
            sum = sum // 10
            curr.next = ListNode(val=i)
            curr = curr.next
        
        return head.next
        
