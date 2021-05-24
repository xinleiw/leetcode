class BaseNode:

    def __init__(self, item):
        self.pre = None
        self.item = item
        self.next = None


class DoubleLinkList:

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        cur = self.__head
        count = 0
        if self.is_empty():
            return 0
        else:
            while cur is not None:
                cur = cur.next
                count += 1
            return count

    def travel(self):
        cur = self.__head
        while cur is not None:
            print(cur.item, end=" ")
            cur = cur.next
        print('')

    def search(self, item):
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                print(item)
                return True
            cur = cur.next
        return False

    def add(self, item):
        node = BaseNode(item)
        node.next = self.__head
        self.__head = node
        if node.next:
            node.next.pre = node

    def append(self, item):
        cur = self.__head
        node = BaseNode(item)
        if self.is_empty():
            self.__head = node
            return
        while cur.next is not None:
            cur = cur.next
        cur.next = node
        node.pre = cur

    def insert(self, pos, item):
        cur = self.__head
        node = BaseNode(item)
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            for i in range(pos - 1):
                cur = cur.next
            node.pre = cur
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        cur = self.__head
        while cur.next is not None:
            if cur.item == item:
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        self.__head.pre = None
                else:
                    cur.pre.next = cur.next
                    if cur.next:
                        cur.next.pre = cur.pre
                return
            cur = cur.next


if __name__ == '__main__':
    ll = DoubleLinkList()
    ll.add(1)
    # print(ll.length())
    ll.append(2)
    ll.append(3)
    ll.add(0)
    ll.insert(3, 1)
    ll.travel()
    ll.remove(1)
    ll.travel()

    print(ll.search(2))

