class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val= val
        self.left=left
        self.right=right
class Solution(object):
    def isSameTree(self,p,q):
        if not p and not q :
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
def main():
    p1 = TreeNode(1)
    p1.left = TreeNode(2)
    p1.right = TreeNode(3)

    q1 = TreeNode(1)
    q1.left = TreeNode(2)
    q1.right = TreeNode(3)

    solution = Solution()
    print(solution.isSameTree(p1, q1))  # Output: True

    # Example 2
    p2 = TreeNode(1)
    p2.left = TreeNode(2)

    q2 = TreeNode(1)
    q2.right = TreeNode(2)

    print(solution.isSameTree(p2, q2))  # Output: False

    # Example 3
    p3 = TreeNode(1)
    p3.left = TreeNode(2)
    p3.right = TreeNode(1)

    q3 = TreeNode(1)
    q3.left = TreeNode(1)
    q3.right = TreeNode(2)

    print(solution.isSameTree(p3, q3))  # Output: False

if __name__ == "__main__":
    main()