#최소 신장 트리(MTS) 그래프의 모든 정점을 연결하는 트리 중에서 간선 가중치의 합
#이 최소인 트리

#최소 연결 비용으로 모든 섬(노드)이 서로 통행 가능하도록 만들 때 

def solution(n,costs):
    
    #cost 현재 다리를 건설하는 비용을 의미함
    #비용을 기준으로 간선을 오름차순 정렬함
    costs.sort(key=lambda x: x[2])
    
    #각 섬의 부모 노드를 저장함
    parent = [i for i in range(n)]
    
    #루트 노드를 찾는 함수
    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node]) # 재귀함수
        return parent[node]
    
    # 두 노드를 합치는 함수
    #초기 상태에서는 모든 노드가 자기 자신으로 가짐
    #루트(집합을 대표하는 노드)가 다르면, 하나의 루트로 통일하여 연결함
    def union(node1,node2):
        
        root1 = find(node1)
        root2 = find(node2)
        
        if root1 != root2:
            parent[root2] = root1
    
    #최소 비용 계산
    answer = 0
    for node1 , node2 , cost in costs:
        if find(node1) != find(node2): # 두 노드가 다른 집합에 속해 있으면
            union(node1,node2) # 두 노드를 연결
            answer += cost # 비용을 추가함
    return answer