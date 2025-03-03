A_num , B_num = map(int,input().split())

A = set(map(int,input().split()))
B = set(map(int,input().split()))

print(len(A-B)) # 차집합의 길이 출력
print(*sorted(list(A-B))) # list - sorted

