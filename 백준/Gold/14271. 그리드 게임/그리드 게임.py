from collections import deque

# 4방향 이동 (상, 우, 하, 좌)
dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]

def simulate_life_game(grid, K):
    """ 무한한 크기의 격자에서 K초 후 살아있는 칸 개수 계산 """
    ROW_OFFSET, COL_OFFSET = 1500, 1500
    found = set()
    q = deque()

    # 초기 살아있는 칸을 큐에 추가
    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'o':  # 살아있는 칸
                found.add((i + ROW_OFFSET, j + COL_OFFSET))
                q.append((i + ROW_OFFSET, j + COL_OFFSET))

    # BFS 탐색 시작
    while K > 0 and q:
        for _ in range(len(q)):  # 현재 depth의 모든 노드 처리
            row, col = q.popleft()
            for i in range(4):
                nextRow, nextCol = row + dRow[i], col + dCol[i]
                if (nextRow, nextCol) not in found:  # 방문하지 않은 곳만 추가
                    found.add((nextRow, nextCol))
                    q.append((nextRow, nextCol))
        K -= 1  # 한 단계 확장 후 K 감소

    return len(found)

# 입력 처리
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]
K = int(input())

# 결과 출력
print(simulate_life_game(grid, K))
