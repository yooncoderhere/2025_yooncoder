# 왼쪽에서 오른쪽으로 이동하는 최소의 비용

#조건: 도로 1km마다 1리터의 기름을 사용함
#더 저렴한 도시가 나오기 전까지 현재 도시에서 기름을 구매해야 최적해 가능함

#최저 가격 변수를 정의해 기름의 최저 가격과 현 기름 가격을 비교

import sys

def solution(N, distance, prices):
    
    min_price = prices[0] # 첫 번째 가격
    total_cost = 0 # 전체 비용
    
    for i in range(N-1):
        #마지막 도시에서는 기름을 살 필요가 없음
        min_price = min(min_price,prices[i]) # 최소 기름 가격
        total_cost += min_price * distance[i] # 최소 가격으로 해당 거리만큼 주유함
    
    return total_cost
    
    
input = sys.stdin.readline
N = int(input().strip()) # 도시 개수
distance = list(map(int,input().split())) # 도로 거리
prices = list(map(int, input().split())) # 기름 가격
print(solution(N,distance,prices))