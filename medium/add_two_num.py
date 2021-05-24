class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new = ListNode()
        head = new
        tail = 0
        while l1 or l2:
            new.next = ListNode()
            new = new.next
            if l1:
                new.val += l1.val
                l1 = l1.next
            if l2:
                new.val += l2.val
                l2 = l2.next
            if tail:
                new.val += tail
            tail = new.val // 10
            if tail:
                new.val = new.val % 10
        else:
            if tail:
                new.next = ListNode(tail)
        return head.next


if __name__ == '__main__':
    solution = Solution()
    result = solution.addTwoNumbers(ListNode(1), ListNode(2))
    print(result.val, result.next)
