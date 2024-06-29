class Solution(object):
    def generate(self, numRows):

        triangle=[[1]]

        for i in range (1,numRows):
            row=[1]
            for j in range(1,i):
                row.append(triangle[i-1][j-1]+ triangle[i-1][j])

            row.append(1)
            triangle.append(row)

        return triangle
def main():
    solution = Solution()
    print(solution.generate(5))  # Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    print(solution.generate(1))  # Output: [[1]]

if __name__ == "__main__":
    main()