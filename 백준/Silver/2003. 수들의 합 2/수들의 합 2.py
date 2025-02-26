#연속된 수들의 부분합 중 합이 M이 되는 경우의 수를 구하는 문제

import sys

input = sys.stdin.readline

N , M = map(int,input().split())
arr = list(map(int,input().split())) # 총 합이 m이 되는 경의 수

#연속되는 숫자 i,j

left , right = 0,0
sum = 0 # 합계
count = 0 # 경우의 수


for right in range(N):
    sum += arr[right]
    
    #저 and 조건은 뭘까
    while sum > M and left <= right:
        sum -= arr[left]
        left +=1
        
    #이 문제의 조건
    if sum == M:
        count += 1
        
print(count)


