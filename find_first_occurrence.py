# NO.28 in leet code  :Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.


def find_first_occurrence(haystack: str, neddle: str) ->int:
    return haystack.find(neddle)

def main():
    haystack1 ="sadbusted"
    neddle1 ='sad'

    out= find_first_occurrence(haystack1,neddle1)

    print('Output:',out)

if __name__=="__main__":
    main()
   

