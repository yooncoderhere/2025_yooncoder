# bfs dfs 이동 
# 현재 위치에서 목표 위치로 이동하려면

import sys
from collections import deque
input = sys.stdin.readline

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1,1,-2,2,-2,2,-1,1]

def bfs(len,start_x,start_y,end_x,end_y):
    queue = deque([(start_x,start_y,0)]) # 방문 좌표 (x,y,나이트 이동 횟수)
    #일반적으로 (x,y)만 넣음
     
    visited = [[False] * len for _ in range(len)] # 방문여부 체크 (좌표)
    visited[start_x][start_y] = True # 시작 좌표 방문 처리
    
    while queue:
        x,y,moves = queue.popleft()
        # 앞에 위치한 걸 다시 빼서
        
        # 목표 위치에 도착한 경우
        if x == end_x and y==end_y:
            return moves
        
        # 나이트를 8가지 방향으로 이동 가능
        for i in range(8):
            nx,ny = x +dx[i], y+dy[i]
            
            if 0 <= nx < len and 0 <= ny < len and not visited[nx][ny]:
                queue.append((nx,ny,moves +1))
                visited[nx][ny] = True
                
T = int(input())
#테스트 케이스의 수

for _ in range(T):
    l = int(input())
    #한 변의 길이
    
    start_x, start_y = map(int, input().split())
    #현재 위치
    end_x, end_y = map(int,input().split())
    #목표 위치
    
    print(bfs(l,start_x,start_y,end_x,end_y))