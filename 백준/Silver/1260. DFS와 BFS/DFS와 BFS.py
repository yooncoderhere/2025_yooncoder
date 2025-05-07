# DFS와 BFS

from collections import deque

#정점의 개수 N
#간선의 개수 M
#정점의 번호 V

#방문할 수 있는 정점이 여러개인 경우
#정점 번호가 작은 것을
#먼저 방문하고 더이상 방문할 수 있는
#점이 없는 경우 종료함

n,m,v = map(int, input().split())
graphs = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)
    
for i in range(1,n+1):
    graphs[i].sort()
    
def dfs(node,visited):
    visited[node] = True
    print(node,end=' ')
    #줄 바꿈
    for neighbor in graphs[node]:
        if not visited[neighbor]:
            dfs(neighbor,visited)
            
def bfs(start):
    visited = [False] *(n+1)
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graphs[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                
#
visited_dfs = [False] * (n+1)
dfs(v,visited_dfs)
print()
bfs(v)

