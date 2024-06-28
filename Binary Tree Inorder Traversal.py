class TreeNode(object):
    def __init__(self, val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution(object):
    def inorderTraversal(self,root):

        result=[]
        stack=[]
        current=root

        while current or stack:
            while current:
                stack.append(current)
                current=current.left

            current= stack.pop()
            result.append(current.val)

            current=current.right
        return result

def main():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    # Create a Solution object
    solution = Solution()

    # Get the inorder traversal
    result = solution.inorderTraversal(root)

    # Print the result
    print(result)  # Output: [1, 3, 2]

if __name__ == "__main__":
    main()