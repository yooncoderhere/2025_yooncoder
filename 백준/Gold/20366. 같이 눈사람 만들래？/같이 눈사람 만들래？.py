import sys
import bisect

def min_snowman_diff(N, snow):
    snow.sort()  # 눈덩이 크기 정렬
    sum_list = []  # 가능한 모든 두 수의 합을 저장할 리스트

    # 모든 두 수(i, j)에 대한 합을 저장 (O(N²))
    for i in range(N - 1):
        for j in range(i + 1, N):
            sum_list.append((snow[i] + snow[j], i, j))  # (합, 인덱스1, 인덱스2)

    sum_list.sort()  # 정렬 (O(N² logN))

    min_diff = float('inf')

    # 가능한 두 개의 눈사람 조합을 찾기 (O(N²))
    for a in range(len(sum_list)):
        sum1, i, j = sum_list[a]

        # 이진 탐색으로 가장 가까운 값 찾기
        idx = bisect.bisect_left(sum_list, (sum1, -1, -1))  # sum1과 같은 값 중 첫 번째 위치

        # 양옆 값 중에서 첫 번째 눈사람과 겹치지 않는 값 찾기
        for b in range(max(0, idx - 2), min(len(sum_list), idx + 2)):
            sum2, k, l = sum_list[b]
            if i != k and i != l and j != k and j != l:  # 서로 겹치는 인덱스가 없어야 함
                min_diff = min(min_diff, abs(sum1 - sum2))

    return min_diff

# 입력 받기
N = int(sys.stdin.readline())
snow = list(map(int, sys.stdin.readline().split()))

# 결과 출력
print(min_snowman_diff(N, snow))
