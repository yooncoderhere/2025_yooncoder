def solution(keyinput, board):
    x, y = 0, 0  # 초기 위치
    max_x, max_y = board[0] // 2, board[1] // 2  # 이동 가능한 최대 범위

    # 방향 매핑
    move = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}

    for key in keyinput:
        dx, dy = move[key]
        new_x, new_y = x + dx, y + dy  # 이동 후 좌표
        
        # 보드 범위를 벗어나지 않도록 조정
        if -max_x <= new_x <= max_x and -max_y <= new_y <= max_y:
            x, y = new_x, new_y

    return [x, y]