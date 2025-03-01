#최소 신장 트리(MTS) 그래프의 모든 정점을 연결하는 트리 중에서 간선 가중치의 합
#이 최소인 트리

#최소 연결 비용으로 모든 섬(노드)이 서로 통행 가능하도록 만들 때 

def solution(n,costs):
    
    #cost 현재 다리를 건설하는 비용을 의미함
    #비용을 기준으로 간선을 오름차순 정렬함
    costs.sort(key=lambda x: x[2])
    
    parent = [i for i in range(n)] # 부모 노드를 저장
    
    #
    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]
    
    def union(node1,node2):
        root1 = find(node1)
        root2 = find(node2)
        
        if root1 != root2:
            parent[root2] = root1
            
    answer = 0
    for node1 , node2 ,cost in costs:
        if find(node1) != find(node2):
            union(node1,node2)
            answer += cost
    return answer