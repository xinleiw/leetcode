class Node:

    def __init__(self, item):
        self.item = item
        # 左侧子节点的索引值
        self.lsub = None
        self.rsub = None


class Tree:

    def __init__(self, node=None):
        self.root = node

    def add(self, elem):
        node = Node(elem)
        if self.root is None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while len(queue) > 0:
                cur = queue.pop(0)
                if not cur.lsub:
                    cur.lsub = node
                    return
                else:
                    queue.append(cur.lsub)
                if not cur.rsub:
                    cur.rsub = node
                    return
                else:
                    queue.append(cur.rsub)
