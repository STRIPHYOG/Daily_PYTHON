class ListNode:
    def __init__(self,val=0, next=None):
        self.val=val
        self.next=next

class Solution:
    def deleteDuplicates(self,head):
        current=head
        while current and current.next:
            if current.val==current.next.val:
                current.next=current.next.next
            else:
                current=current.next
        return head
    
def list_to_linkedlist(item):
    if not item:
        return None
    head= ListNode(item[0])
    current=head
    for items in item[1:]:
        current.next = ListNode(items)
        current = current.next
    return head
def linkedlist_to_list(head):
    items = []
    current = head
    while current:
        items.append(current.val)
        current = current.next
    return items
def main():
    input_list1 = [1, 1, 2]
    input_list2 = [1, 1, 2, 3, 3]

    head1 = list_to_linkedlist(input_list1)
    head2 = list_to_linkedlist(input_list2)

    solution = Solution()
    output_head1 = solution.deleteDuplicates(head1)
    output_head2 = solution.deleteDuplicates(head2)

    print(linkedlist_to_list(output_head1))  # Output: [1, 2]
    print(linkedlist_to_list(output_head2))  # Output: [1, 2, 3]

if __name__ == "__main__":
    main()
