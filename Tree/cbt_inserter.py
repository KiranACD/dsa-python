from collections import namedtuple
from collections import namedtuple
from make_tree import MakeTree
from treenode import TreeNode

class CBTInserter:
    def __init__(self, root):
        self.root = root
        self.TreeInfo = namedtuple('TreeInfo', 'height is_inserted parent_val')

    def is_last_level_filled(self, lnode, rnode):
        if lnode is None and rnode is None:
            return True
        if lnode is None or rnode is None:
            return False
        return self.is_last_level_filled(lnode.left, rnode.right)
    
    def insert_node(self, root, node):
        if root.right is None:
            print('first')
            root.right = node
            return root.val
        root = root.right
        while (root):
            if root.left is None:
                root.left = node
                return root.val
            elif root.right is None:
                root.right = node
                return root.val
            else:
                root = root.left
                
    def find_height_diff_insert(self, root, node):
        if root is None:
            return self.TreeInfo(-1, False, None)
        
        left = self.find_height_diff_insert(root.left, node)
        right = self.find_height_diff_insert(root.right, node)
        
        height = max(left.height, right.height) + 1
        
        if left.is_inserted or right.is_inserted:
            val = left.parent_val if left.parent_val is not None else right.parent_val
            return self.TreeInfo(height, True, val)
            
        if left.height != right.height:
            print(root.val)
            val = self.insert_node(root, node)
            return self.TreeInfo(height, True, val)
        
        return self.TreeInfo(height, False, None)
        
    def insert(self, val):
        node = TreeNode(val)
        if self.is_last_level_filled(self.root.left, self.root.right):
            curr_node = self.root
            while curr_node.left: 
                curr_node = curr_node.left
            curr_node.left = node
            return curr_node.val
        else:
            info = self.find_height_diff_insert(self.root, node)
            print(info.is_inserted)
            return info.parent_val
            
    def get_root(self):
        return self.root

if __name__ == "__main__":

    lst = input('Enter list: ')
    lst = [int(i) for i in lst.split()]
    tree = MakeTree(lst)
    root = tree.get_root()
    tree.print_tree(root)
    inserter = CBTInserter(root)
    print('--------------------------------------------')
    print(inserter.get_root().val)
    print('--------------------------------------------')
    n = int(input('num inserts: '))
    for _ in range(n):
        num = int(input('Enter: '))
        print('--------------------------------------------')
        val = inserter.insert(num)
        print(val)
        print('--------------------------------------------')
        tree.print_tree(root)
        