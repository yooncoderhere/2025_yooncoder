#갈색 테두리가 노란색을 감싸는 형태이므롷 

def solution(brown, yellow):
    total_tiles = brown + yellow  # 전체 카펫 크기 (w × h)

    # 1. 가능한 모든 가로(w) & 세로(h) 조합 찾기
    for w in range(3, int(total_tiles**0.5) + 2):  # 최소 3부터 시작
        if total_tiles % w == 0:  # 나누어 떨어지면 후보
            h = total_tiles // w  # 세로 계산
            if (w - 2) * (h - 2) == yellow:  # 노란색 타일 개수 확인
                return [max(w, h), min(w, h)]  # 가로 ≥ 세로 유지
