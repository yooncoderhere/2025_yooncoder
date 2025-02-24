import sys
input = sys.stdin.readline

N,K = map(int,input().split()) # N개의 줄 , 가치의 합 K
coins = [int(input()) for _ in range(N)]

coins.reverse() # 기존에 오름차순으로 받았기 때문에 리스트 뒤집음

count = 0
for coin in coins:
    if K == 0:
        break
    count += K // coin
    K %= coin # 남은 금액
    
print(count)
    
