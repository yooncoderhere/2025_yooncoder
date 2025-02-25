# 주식을 사고 팔아서 최대 이익을 얻는 문제
#오른쪽에서 왼쪽으로 순회하면서 최고 가격을 갱신
#현재 가격이 max_price보다 작으면 매수 크면 그대로 유지함


def solution(values_arr):
    max_price = 0 # 최대 주가
    profit = 0 # 총 이익
    
    #뒤에서부터 탐색
    for i in range(len(values_arr)-1,-1,-1):
        max_price = max(max_price,values_arr[i]) #최고 주가
        if values_arr[i] < max_price: # 현재 가격이 최고가보다 낮으면 매수 후 판매
            profit += max_price - values_arr[i] #이익
        
    return profit
    
import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스

for _ in range(T):
    N = int(input()) # 날의 수 - 안쓰네..
    values_arr = list(map(int,input().split()))
    print(solution(values_arr))
    