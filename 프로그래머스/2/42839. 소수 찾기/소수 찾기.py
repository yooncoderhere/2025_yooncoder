from itertools import permutations

#각 숫자로 만들 수 있는 숫자 조합을 찾고 -> 그 다음에 그 중에서 소수인 숫자 개수를 반환
#중복된 순자는 같은 숫자임 11 = 011

def is_prime(n):
    if n<2:
        return False
    #0과 1은 소수가 아님
    for i in range(2,int(n**0.5)+1):
        if n % i == 0: # 나눠지면 소수가 아님
            return False
    return True

def solution(numbers):
    prime_numbers = set() # 중복 방지를 위해 set을 사용
    
    for length in range(1,len(numbers)+1): # 길이 1부터 N까지
        #숫자를 조합해서 순서가 다른 모든 경우를 생성
        for perm in permutations(numbers,length):
            num = int("".join(perm)) # 리스트를 숫자로 변환
            
            if is_prime(num): # 소수인지 판별함
                prime_numbers.add(num) # 중복 제거 후 저장

    return len(prime_numbers) # 소수개수 반환