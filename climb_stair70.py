class Solution:
    def climbStair(self, n: int):
        if n==1:
            return 1
        elif n==2:
            return 2
        

        dp=[0]*(n+1)
        dp[1]=1
        dp[2]=2

        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]

        return dp[n]
    
def main():
    soluation= Solution()
    casetext=[2, 3, 4, 5, 6]
    for n in casetext:
        ways =soluation.climbStair(n)
        print(f"number of climbs:{ways}")
if __name__=="__main__":
    main()