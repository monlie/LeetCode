# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        h = ListNode(0)
        h.next = head
        mark = h
        pr = head
        for i in range(n):
            pr = pr.next
        while pr:
            pr = pr.next
            mark = mark.next
        mark.next = mark.next.next
        return h.next
        