import sys

#트럭 한대로 배송할 수 있는 최대 박스 수를 한 줄에 출력함
def solution(N,C,deliveries):
    
    # 1. 먼저 도착하는 택배부터 배달을 완료해야 트럭 공간을 효율적으로 사용할 수 있음
    deliveries.sort(key=lambda x : (x[1],x[0]))
    
    # 2. 각 마을별 트럭 용량 추적 배열
    load = [0] * (N+1)
    total_delivered  = 0
    
    for frm , to , boxes in deliveries:
        #트럭에 실을 수 있는 개수 확인
        max_deliverise = min(boxes, C-max(load[frm:to]))
        for i in range(frm, to):
            load[i] += max_deliverise # 실을 수 있는 만큼 최대한 실어줌
        
        total_delivered += max_deliverise # 최종 배달한 박스의 수
    
    return total_delivered

input = sys.stdin.readline
N , C = map(int,input().split()) # 마을 수 , 트럭의 용량
M = int(input()) # 보내는 박스 정보의 개수

#보내는 마을 번호, 박스를 받는 마을 번호, 보내는 박스 개수 3가지 값을 tuple로 받음
#출발이 아니라, 도착지 기준으로 정렬 해야 최대한 많은 박스를 싣을 수 있음
deliveries = [tuple(map(int,input().split())) for _ in range(M)]
print(solution(N,C,deliveries))