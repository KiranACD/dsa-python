from collections import deque, namedtuple


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

def prob1(A):
    
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

def prob2(A, B, C):

    TreeInfo = namedtuple('TreeInfo', 'h1 h2 d')

    def get_dist(root):
        if root is None:
            return TreeInfo(None, None, None)
        
        left = get_dist(root.left)
        right = get_dist(root.right)

        print('-----------------------------------------')
        print(root.val, left, right)

        if left.d is not None or right.d is not None:
            d = left.d if left.d is not None else right.d
            h1 = left.h1 if left.h1 is not None else right.h1
            h2 = left.h2 if left.h2 is not None else right.h2
            print(root.val, h1, h2, d)
            return TreeInfo(h1, h2, d)

        if left.h1 is not None and right.h2 is not None:
            d = left.h1 + right.h2
            print(left.h1, right.h2, d)
            return TreeInfo(left.h1+1,right.h2+1,d)
        elif left.h2 is not None and right.h1 is not None:
            d = left.h2 + right.h1
            print(right.h1, left.h2, d)
            return TreeInfo(right.h1+1,left.h2+1,d)
        elif left.h1 is not None and root.val == C:
            print(left.h1, 0, left.h1)
            return TreeInfo(left.h1+1, 1, left.h1+1)
        elif right.h1 is not None and root.val == C:
            print(right.h1, 0, right.h1)
            return TreeInfo(right.h1+1, 1, right.h1+1)
        elif left.h2 is not None and root.val == B:
            print(0, left.h2, left.h2)
            return TreeInfo(1, left.h2 + 1, left.h2+1)
        elif right.h2 is not None and root.val == B:
            print(0, right.h2, right.h2)
            return TreeInfo(1, right.h2+1, right.h2+1)
        else:
            d = None
        
        if root.val == B and left.h1 is None and right.h1 is None:
            h1 = 1
        elif left.h1 is not None or right.h1 is not None:
            h1 = left.h1+1 if left.h1 is not None else right.h1+1
        else:
            h1 = None
        
        if root.val == C and left.h2 is None and right.h2 is None:
            h2 = 1
        elif left.h2 is not None or right.h2 is not None:
            h2 = left.h2+1 if left.h2 is not None else right.h2+1
        else:
            h2 = None
        
        print(root.val, h1, h2)
        return TreeInfo(h1, h2, d)
    
    tree = get_dist(A)
    return tree.d
    
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
    print(prob2(root, 35, 10))
    