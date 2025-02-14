def solution(board):
    n = len(board)
    danger = [[False] *n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            #지뢰
            if board[i][j] == 1:
                for dx in [-1,0,1]: # 위, 같은행 , 아래
                    for dy in [-1,0,1]: # 왼쪽 , 같은 열, 오른쪽으로 이동
                        ni, nj = i + dx, j +dy
                        if 0<= ni <n and 0 <= nj <n:
                            danger[ni][nj] =True
                            
    safe_count = 0
    for i in range(n):
        for j in range(n):
            if not danger[i][j] and board[i][j] == 0:
                safe_count +=1
    
    return safe_count