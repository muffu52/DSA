class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.v:
            return node
        elif (val < node.v and node.l is not None):
            return self._find(val, node.l)
        elif (val > node.v and node.r is not None):
            return self._find(val, node.r)

    def deleteTree(self):
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)

    def _minimum(self,x):
        while x.l is not None:
            x = x.l
        return x

    def _parentVal(self, node, x):
        if (node.l and node.l.v == x.v) or (node.r and node.r.v == x.v):
            return node
        else:
            if node.l is not None:
                return self._parentVal(node.l , x)
            if node.r is not None:
                return self._parentVal(node.r , x)

    def successor(self, val):
        x = self.find(val)
        if x is not None:
            if x.r is not None:
                return self._minimum(x.r).v
        else:
            return None
        y = self._parentVal(self.root, x)
        while y is not None and x == y.r:
            x = y
            y = self._parentVal(self.root, y)
            return y.v
        

tree = Tree()

tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
print(tree.find(3).v)
# print(tree.find(10))

print(tree.successor(10))
tree.deleteTree()
tree.printTree()