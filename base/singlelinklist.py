
class BaseNode:

    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList:

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur is not None:
            print(cur.item, end=" ")
            cur = cur.next
        print("")

    def search(self, item):
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                print(cur.item)
                return True
            cur = cur.next
        return False

    def add(self, item):
        # 插头增
        node = BaseNode(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        node = BaseNode(item)
        if self.is_empty():
            self.__head = node
        cur = self.__head
        while cur.next is not None:
            cur = cur.next
        cur.next = node

    def insert(self, pos, item):
        node = BaseNode(item)
        if pos >= self.length():
            self.append(item)
        elif pos <= 0:
            self.add(item)
        else:
            cur = self.__head
            for i in range(pos-1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.item == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                return
            pre = cur
            cur = cur.next


if __name__ == '__main__':
    ll = SingleLinkList()
    ll.add(1)
    ll.travel()

    print(ll.length())
    ll.add(2)
    print(ll.length())
    ll.append(3)
    print(ll.length())
    ll.insert(2, 5)
    # ll.insert(3, 6)
    # ll.insert(4, 5)
    print(ll.length())
    # ll.remove(5)
    ll.travel()






