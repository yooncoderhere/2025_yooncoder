def solution(m, n, puddles):
    MOD = 1000000007
    dp = [[0]*m for _ in range(n)]

    #시작 지점
    dp[0][0] = 1
    
    # list가 아닌 Set에 저장해서 물웅덩이인지 빠르게 확인 
    puddles = set((y-1, x-1) for x, y in puddles)

    for i in range(n):
        for j in range(m):
            #
            if (i, j) in puddles:
                dp[i][j] = 0
                continue

            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]

            dp[i][j] %= MOD

    return dp[n-1][m-1]
