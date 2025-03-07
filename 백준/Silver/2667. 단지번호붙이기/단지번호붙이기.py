import sys
from collections import deque

input = sys.stdin.readline

N = int(input()) # 지도 크기

graph = [list(map(int,input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution(x,y):
    queue = deque([(x,y)])
    visited[x][y] = True
    count = 1
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4): # 네 방향 탐색
            nx,ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] ==1:
                queue.append((nx,ny))
                visited[nx][ny] = True
                count +=1 # 집 개수 증가
    return count

home = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            home.append(solution(i,j)) # count 추가
            
home.sort()
print(len(home)) # 총 단지 수 출력
print("\n".join(map(str,home))) # 각 단지내의 집의 수를 한줄에 하나씩 출력력

