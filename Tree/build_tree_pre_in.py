'''
Given the preorder and inorder traversal of a tree. Construct the tree. (No duplicates)
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BuildTree:
    def __init__(self, preorder, inorder):
        self.preorder = preorder
        self.inorder = inorder
        self.num_nodes = len(self.preorder)

    def get_inorder_map(self):
        self.map = {}
        for _ in range(self.num_nodes):
            self.map[self.inorder[_]] = _

    def build_tree(self, s_pre, e_pre, s_in, e_in):        
        if s_in > e_in:
            return None
        
        root = Node(self.preorder[s_pre])
        r_index = self.map[self.preorder[s_pre]]
        root.left = self.build_tree(s_pre+1, s_pre+r_index-s_in, s_in, r_index-1)
        root.right = self.build_tree(s_pre+r_index-s_in+1, e_pre, r_index+1, e_in)

        return root
    
    def get_root(self):
        self.get_inorder_map()
        self.root = self.build_tree(0, self.num_nodes-1, 0, self.num_nodes-1)

    
