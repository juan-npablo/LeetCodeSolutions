# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_l1 = self.runLinkedList(l1)
        result_l2 = self.runLinkedList(l2)
        total = result_l1 + result_l2
        answer_list = []
        while total >= 10:
            answer_list.insert(0, total % 10)
            total = total // 10
        result = ListNode(total)
        for i in answer_list:
            result = ListNode(i, result)
        return result

    def runLinkedList(self, head: Optional[ListNode]):
        actual = head
        result = 0
        index = 1
        while actual is not None:
            result += actual.val * index
            index *= 10
            actual = actual.next
        return result