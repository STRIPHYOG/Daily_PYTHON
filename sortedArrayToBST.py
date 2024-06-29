# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # Helper function to convert array to BST
        def convertListToBST(left, right):
            if left > right:
                return None

            # Always choose middle element to ensure height-balanced
            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            # Recursively build the left and right subtrees
            node.left = convertListToBST(left, mid - 1)
            node.right = convertListToBST(mid + 1, right)
            return node

        # Convert the whole array to BST
        return convertListToBST(0, len(nums) - 1)

def main():
    solution = Solution()

    # Example 1
    nums1 = [-10, -3, 0, 5, 9]
    tree1 = solution.sortedArrayToBST(nums1)
    print(tree1)  # Output: [0, -3, 9, -10, null, 5]

    # Example 2
    nums2 = [1, 3]
    tree2 = solution.sortedArrayToBST(nums2)
    print(tree2)  # Output: [3, 1]

if __name__ == "__main__":
    main()
