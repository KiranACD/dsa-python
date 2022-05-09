from collections import namedtuple, deque
from treenode import TreeNode

class MakeTree:

    def __init__(self, lst):
        self.lst = lst
        self.root = None
    
    def build_tree(self):
        q = deque()
        self.root = TreeNode(self.lst[0])
        node = self.root
        q.append(node)
        i = 1
        while q:
            node = q.popleft()
            val1 = self.lst[i]
            i += 1
            val2 = self.lst[i]
            i += 1
            if val1 != -1:
                node1 = TreeNode(val1)
                node.left = node1
                q.append(node1)
            if val2 != -1:
                node2 = TreeNode(val2)
                node.right = node2
                q.append(node2)
    
    def get_root(self):
        self.build_tree()
        return self.root
    
    def print_tree(self, root):
        if root is None:
            return
        self.print_tree(root.left)
        print(root.val)
        self.print_tree(root.right)