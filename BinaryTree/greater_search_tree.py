
from binary_tree import ConstructBinaryTree

class Solution:
    node_sum = 0

    @staticmethod
    def convertBST(root):
        
        def bst(node):
            if node is None:
                return
            
            bst(node.right)
            
            Solution.node_sum +=  node.val
            node.val = Solution.node_sums
            
            bst(node.left)

            return
        
        bst(root)
        return root

if __name__ == '__main__':
    arr = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
    maketree = ConstructBinaryTree(arr)
    maketree.start()

    sol = Solution()
    sol.convertBST(maketree.root)
    

