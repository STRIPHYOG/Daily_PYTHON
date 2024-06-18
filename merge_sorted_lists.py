#merge two sorted list
def merge_sorted_lists(list1,list2):
    merge_list = []
    i = j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merge_list.append(list1[i])
            i=i+1
        else:
            merge_list.append(list2[j])
            j=j+1
            
            
    merge_list.extend(list1[i:])
    merge_list.extend(list2[j:])
    
    return merge_list


def main():
    list1 = [1, 3, 5, 7]
    list2 = [2, 4, 6, 8]
    
    merge_list = merge_sorted_lists(list1,list2)
    print("Merge list:", merge_list)
    
if __name__ == "__main__":
    main()
