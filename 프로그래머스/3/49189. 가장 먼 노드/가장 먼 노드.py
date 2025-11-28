from collections import deque

def solution(n, edge):
    
    g = [[] for _ in range(n+1)] # 그래프 생성
    
    for a,b in edge:
        g[a].append(b)
        g[b].append(a)
        
    dist = [-1]*(n+1)
    dist[1] = 0
    q = deque([1])
    
    while q:
        v = q.popleft()
        
        for nv in g[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v]+1
                q.append(nv)
                
    return dist.count(max(dist))
    
    
    
    answer = 0
    return answer