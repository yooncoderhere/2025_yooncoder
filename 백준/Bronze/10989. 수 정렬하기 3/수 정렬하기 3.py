import sys

# 입력 빠르게 받기
input = sys.stdin.readline

# 입력받기
N = int(input())  
count = [0] * 10001  # 1부터 10,000까지 등장 횟수 저장

# 숫자 카운트
for _ in range(N):
    num = int(input())
    count[num] += 1

# 정렬된 값 출력
for i in range(10001):  # 1부터 10,000까지 순회
    if count[i] > 0:
        for _ in range(count[i]):  
            print(i)
