# 하나 이상의 연속된 소수의 합으로 나타낼 수 있는 자연수들이 존재함
# 조건 1. 소수 2. 연속 소수
import sys

def primes(n):
    is_primes = [True] * (n+1)
    is_primes[0] = is_primes[1] = False 
    # 0과 1은 소수가 아님
    
    for i in range(2,int(n**0.5)+1):
        if is_primes[i]:
            for j in range(i*i,n+1,i):
                is_primes[j] = False
    return [i for i in range(n+1) if is_primes[i]]

def sum_primes(n):
    prime = primes(n)
    # 소수리스트 받기
    start, end, count = 0,0,0
    # 투 포인터 설정
    
    total = 0 
    #부분합
    
    while end <=len(prime):
        if total < n:
            if end < len(prime):
                total += prime[end]
            end += 1 # 하나의 소수를 더함
            
        elif total > n :
            #부분합이 n 보다 큰 경우
            total -= prime[start]
            # 연속된 소수의 합을 구하는 것이니까
            # 앞의 소수를 제거
            start += 1
            # 제거 후 포인터 값 증가
        else:
            count +=1
            # 연속된 소수의 합으로 나타낼 수 있는 경우의 수 추가
            total -= prime[start]
            #
            start += 1
            #포인터 이동
            
    return count

input= sys.stdin.readline
N = int(input())
print(sum_primes(N))


