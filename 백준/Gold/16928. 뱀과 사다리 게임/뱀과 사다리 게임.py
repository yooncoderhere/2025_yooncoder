#뱀과 사다리 게임

# 주사위를 돌려서 나오는 수만큼 이동
# 1번 칸에서 시작해서 100번 칸에 도착하면 종료
# 사다리 또는 뱀이 있는 칸에 도착하면
# 사다리 또는 뱀을 타고 이동

import sys
input = sys.stdin.readline

#입력 받기
n, m = map(int, input().split())
#n 사다리의 수
#m 뱀의 수

#사다리 정보 저장 x,y
ladder = {}
for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

#뱀 정보 저장 x,y
snake = {}
for _ in range(m):
    x, y = map(int, input().split())
    snake[x] = y

#방문 여부 확인
visited = [False] * 101

#bfs 탐색
from collections import deque

def bfs(start):
    queue = deque([(start, 0)])  # (위치, 이동 횟수)
    visited[start] = True
    
    while queue:
        pos, count = queue.popleft()
        
        if pos == 100:
            return count
        
        for i in range(1, 7):
            next_pos = pos + i
            
            if next_pos > 100:
                continue
            # 100을 넘어가면 무시
            
            if visited[next_pos]:
                continue
            # 이미 방문한 위치면 무시
            
            # 사다리가 있는 경우
            if next_pos in ladder:
                next_pos = ladder[next_pos]
            # 뱀이 있는 경우
            elif next_pos in snake:
                next_pos = snake[next_pos]
            
            visited[next_pos] = True
            queue.append((next_pos, count + 1))
    
    return -1

print(bfs(1))   
