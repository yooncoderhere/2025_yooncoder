
import sys
from collections import deque

input = sys.stdin.readline

# 나이트 이동 방향
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs(l, start_x, start_y, end_x, end_y):
    queue = deque([(start_x, start_y, 0)])  # (x, y, 이동 횟수)
    visited = [[False] * l for _ in range(l)]  # 방문 여부 체크
    visited[start_x][start_y] = True  # 시작 위치 방문 처리

    while queue:
        x, y, moves = queue.popleft()

        # 목표 위치에 도착하면 이동 횟수 반환
        if x == end_x and y == end_y:
            return moves
        
        # 8가지 방향으로 이동
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            # 체스판 범위를 벗어나지 않고, 방문하지 않은 경우
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                queue.append((nx, ny, moves + 1))
                visited[nx][ny] = True  # 방문 처리

T = int(input()) 

for _ in range(T):
    L = int(input())  # 체스판 크기
    start_x, start_y = map(int, input().split())  # 시작 위치
    end_x, end_y = map(int, input().split())  # 목표 위치

    # 결과 출력
    print(bfs(L, start_x, start_y, end_x, end_y))
