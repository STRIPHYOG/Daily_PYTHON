# def plusOne(digits):
#      num= int(''.join(map(str,digits))) +1
#      return list(map(int, str(num)))
# def main():
#      tc=[[1, 2, 3],[4, 3, 2, 1],[9]]

#      for digits in tc:
#           result = plusOne(digits)
#           print(result)

# if __name__=='__main__':
#      main()
class NumberArray:
    def __init__(self, digits):
        self.digits = digits

    def increment(self):
        num = int("".join(map(str, self.digits))) + 1
        self.digits = list(map(int, str(num)))

    def print_array(self):
        print(self.digits)

def main():
    test_cases = [
        [1, 2, 3],  
        [4, 3, 2, 1],  
        [9]  
    ]

    for digits in test_cases:
        num_array = NumberArray(digits)
        num_array.increment()
        print(f"Input: {digits}, Output: ", end="")
        num_array.print_array()

if __name__ == "__main__":
    main()
