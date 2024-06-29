class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution(object):
    def maxDepth(self,root):
        if not root:
            return 0
        else:
            left_depth=self.maxDepth(root.left)
            right_depth=self.maxDepth(root.right)
            return max(left_depth, right_depth)+1
        
def main():
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)

    solution = Solution()
    print("root depth",solution.maxDepth(root1))  # Output: 3

    # Example 2
    root2 = TreeNode(1)
    root2.right = TreeNode(2)

    print('root depth',solution.maxDepth(root2))  # Output: 2

if __name__ == "__main__":
    main()
