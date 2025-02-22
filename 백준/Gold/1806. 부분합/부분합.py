import sys
#큐가 아니라 투포인터로 푸는게 나음

#합이 s이상 되는 것 중 가장 짧은 것의 길이를 구하는 프로그램

#수열의 길이 N과 이 수열의 부분합이 S 이상은 되어야 함
# S이상을 만족하는 것들 중 가장 짧은 수열의 길이를 반환함

input = sys.stdin.readline
n , s = map(int,input().split())
arr = list(map(int, input().split()))

left, right = 0,0
sum_sub = 0 # 합
min_len = n+1

#수열의 길이 n보다 작으면
while right < n:
    sum_sub += arr[right] # 오른쪽 포인터 이동
    
    #부분 수열의 합이 s보다 작아야 하기 때문에
    while sum_sub >=s:
        #현재 부분 배열의 길이를 구하는 공식
        min_len = min(min_len, right -left+1) # right -left +1
        sum_sub -=arr[left] # 좌측값 빼줌
        left +=1 # 왼쪽 포인터 이동
        
    right +=1 # 우측 이동
    
print(min_len if min_len != n+1 else 0)

        
        
        
    
