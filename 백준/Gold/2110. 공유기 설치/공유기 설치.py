import sys

#이 문제 풀면서 궁금했던 점: 공유기 1개가 몇개까지 커버치는지가 궁금했는데 문제 방향이랑은 크게 상관이 없음
#이분 탐색으로 풀어야겠다는 생각은 못하고 각 공유기의 지점을 포인터로 지정해야 하나 생각함
# 유의: prev, cnt 변수 지정
# 공유기의 개수를 기반으로 두 공유기 사이의 최대 거리를 조절함

def solution(N, C, house_list):
    house_list.sort()  # 집 좌표 정렬
    left, right = 1, house_list[-1] - house_list[0]  # 최소 거리, 최대 거리
    answer = 0  # 최적의 거리

    while left <= right:
        mid = (left + right) // 2  # 중간값
        prev, cnt = house_list[0], 1  # 첫 번째 집에 공유기 설치,
        # 현재 설치한 공유기의 개수 cnt

        for i in range(1, N):
            if house_list[i] - prev >= mid:  # mid 이상의 거리 확보 시 공유기 설치
                cnt += 1
                prev = house_list[i] 
                # 마지막으로 공유기가 설치된 위치를 갱신함

        if cnt >= C:  # 설치된 공유기 개수가 기존에 받은 것보다 많거나 같으면
            answer = mid  # mid 값을 최적 거리 후보로 두고
            left = mid + 1 #거리를 늘려봄
        else:  # 공유기 개수가 부족하면 거리 줄이기
            right = mid - 1

    return answer  # 최적 거리 반환

# 입력 처리
input = sys.stdin.readline
N, C = map(int, input().split())
house_list = [int(input().strip()) for _ in range(N)]

# 결과 출력
print(solution(N, C, house_list))
