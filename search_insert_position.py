#Q35:leetcode-> Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

from typing import List

def search_insert_position(num: List[int], target:int ) -> int:
    left=0
    right=len(num)-1
    while left<=right:
        mid= left+(right-left)//2
        if num[mid] == target:
            return mid
        elif num[mid]< target:
            left= mid+1
        else:
            right=mid-1
    return left
def main():
    num=[1,2,3,4,5,6,7]
    target= 5
    out= search_insert_position(num,target)

    print('Output:',out)

if __name__=="__main__":
    main()




