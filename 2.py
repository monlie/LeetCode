# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c = 0
        head = ListNode('Head')
        last = head
        
        while l1 and l2:
            s = (l1.val + l2.val + c)
            num = s % 10
            c = s // 10
            last.next = ListNode(num)
            last = last.next
            l1 = l1.next
            l2 = l2.next
            
        if not l1:
            l1 = l2
            
        while l1:
            s = (l1.val + c)
            num = s % 10
            c = s // 10
            last.next = ListNode(num)
            last = last.next
            l1 = l1.next
        
        if c:
            last.next = ListNode(c)
        
        return head.next
        