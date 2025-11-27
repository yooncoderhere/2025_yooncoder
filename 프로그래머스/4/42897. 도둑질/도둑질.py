# 인접한 두 곳은 안됨

def solution(money):
    
    def cir(arr):
        dp1,dp2 = 0,0
        
        for x in arr:
            #
            dp1, dp2 = dp2, max(dp2,dp1 + x)
        return dp2
# 첫번째 집 포함 , 마지막 집 제외
    case1 = cir(money[:-1])

# 첫 집 제외하고 , 마지막 집 포함
    case2 = cir(money[1:]) 

    return max(case1,case2)