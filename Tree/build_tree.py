from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(lst):

    q = deque()
    root = TreeNode(lst[0])
    node = root
    q.append(node)
    i = 1
    while q:
        node = q.popleft()
        val1 = lst[i]
        i += 1
        val2 = lst[i]
        i += 1
        if val1 != -1:
            node1 = TreeNode(val1)
            node.left = node1
            q.append(node1)
        if val2 != -1:
            node2 = TreeNode(val2)
            node.right = node2
            q.append(node2)
    
    return root

def prob(A):
    
    ans = []
    ans_set = set()
    q = deque()
    q.append(A)
    nodes = []
    while q:
        size = len(q)
        level = []
        for _ in range(size):
            node = q.popleft()
            if _ == 0:
                print('left: ', node.val)
                ans.append(node)
                ans_set.add(node)
            level.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        nodes.append(level)
    
    def preorder(root):
        if root is None:
            return None
        if root.left is None and root.right is None:
            if root not in ans_set:
                print('bottom: ',root.val)
                ans.append(root)
                ans_set.add(root)
        preorder(root.left)
        preorder(root.right)
    
    preorder(A)

    for _ in range(len(nodes)-1, -1, -1):
        if nodes[_][-1] not in ans_set:
            print('right: ', nodes[_][-1].val)
            ans.append(nodes[_][-1])
            ans_set.add(nodes[_][-1])
    
    ans = [node.val for node in ans]
    return ans

def print_inorder(root):
    if root is None:
        return
    print_inorder(root.left)
    print(root.val)
    print_inorder(root.right)

if __name__ == '__main__':

    lst = input('Enter the list: ')

    lst = [int(i) for i in lst.split()]

    root = build_tree(lst)
    print(prob(root))