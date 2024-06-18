def remove_number(num,val):
    k=0
    for i in range(len(num)):
        if num[i] != val:
            num[k] =num[i]
            k=k+1
    return k

def main():
    num=[3,2,2,3,4]
    val=3
    print(remove_number(num,val)) #out
    print(num[:5])

if __name__=="__main__":
    main()