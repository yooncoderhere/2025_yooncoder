import sys

def solve():
    N = int(sys.stdin.readline())  # 탑 개수
    heights = list(map(int, sys.stdin.readline().split()))  # 탑 높이 리스트
    result = [0] * N  # 결과 저장 (0으로 초기화)
    stack = []  # 스택 (탑의 인덱스 저장)

    for i in range(N):
        while stack and heights[stack[-1]] < heights[i]:  # 현재 탑보다 낮은 탑 제거
            stack.pop()
        
        if stack:  # 스택이 비어있지 않다면, 가장 가까운 왼쪽 탑이 레이저를 수신
            result[i] = stack[-1] + 1  # 1-based index 변환

        stack.append(i)  # 현재 탑 인덱스 스택에 저장

    print(" ".join(map(str, result)))  # 결과 출력

# 입력이 많을 수 있으므로 sys.stdin 사용
if __name__ == "__main__":
    solve()
