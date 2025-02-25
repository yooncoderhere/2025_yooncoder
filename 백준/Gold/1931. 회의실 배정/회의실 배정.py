
#더 많은 회의를 배정하기 위해서
#종료 시간이 빠른 회의를 우선 선택
#종료 시간이 같으면, 시작 시간이 빠른 회의를 먼저 배치

import sys

input = sys.stdin.readline

N = int(input())
#튜플로 두 개의 값을 받음 - 고정된 데이터
schedules = [tuple(map(int,input().split())) for _ in range(N)]

# 종료 시간 - 시작 시간 순으로 정렬
schedules.sort(key=lambda x: (x[1],x[0]))

count = 0 # 최대 회의 개수
last_time = 0 # 이전 회의 종료 시간

#그리디 방식으로 회의 선택함
for start, end in schedules:
    if start >= last_time:
        count += 1
        last_time = end # 회의 종료 시간 업데이트

print(count)