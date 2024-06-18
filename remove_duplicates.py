def remove_duplicates(sorted_list):
    return list(dict.fromkeys(sorted_list))
           # dict.formkeys method always short the list 
def main():
    sorted_list=[1,1,2,3,3,4,4,4,5,6,7]
    new_list= remove_duplicates(sorted_list)
    print("list without duplicates:", new_list)

if __name__=="__main__":
    main()
    
