# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def checkBalance(node):
            if not node:
                return 0, True
            
            left_height, left_balanced = checkBalance(node.left)
            right_height, right_balanced = checkBalance(node.right)
            
            current_height = 1 + max(left_height, right_height)
            current_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            
            return current_height, current_balanced
        
        _, is_balanced = checkBalance(root)
        return is_balanced

def main():
    # Example 1
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20, TreeNode(15), TreeNode(7))

    # Example 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3))
    root2.right = TreeNode(2)

    # Example 3
    root3 = None

    solution = Solution()
    print(solution.isBalanced(root1))  # Output: True
    print(solution.isBalanced(root2))  # Output: False
    print(solution.isBalanced(root3))  # Output: True

if __name__ == "__main__":
    main()
