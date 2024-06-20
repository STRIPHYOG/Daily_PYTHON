class BinaryAdder:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add_binary(self):
        result =[]
        cary=0
        i= len(self.a)-1
        j= len(self.b)-1

        while i>=0 or j>=0 or cary:
            total=cary
            if i>=0:
                total=total+int(self.a[i])
                i=i-1
            if j>=0:
                total=total+int(self.b[j])
                j=j-1
            result.append(str(total%2))
            cary= total//2
        return ''.join(result[::-1])
    
def main():
    test_cases = [
        ("11", "1"),  # Expected output: "100"
        ("1010", "1011"),  # Expected output: "10101"
        ("1111", "1111")  # Expected output: "11110"
    ]

    for a, b in test_cases:
        binary_adder = BinaryAdder(a, b)
        result = binary_adder.add_binary()
        print(f"Adding {a} and {b}: {result}")

if __name__ == "__main__":
    main()
                

        
    