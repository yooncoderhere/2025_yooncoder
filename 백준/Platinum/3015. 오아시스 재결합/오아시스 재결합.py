import sys

def count_visible_pairs(n, heights):
    stack = []
    result = 0

    for h in heights:
        count = 1  # 현재 사람의 개수 (동일한 키가 연속으로 있는 경우)
        
        # 스택의 top보다 키가 크면 pop하면서 카운트 증가
        while stack and stack[-1][0] <= h:
            height, cnt = stack.pop()
            result += cnt  # pop된 사람들은 현재 사람과 볼 수 있음
            
            if height == h:  # 같은 키면 개수 누적
                count += cnt
        
        # 스택에 현재 사람 추가
        if stack:
            result += 1  # 현재 사람은 스택의 top과도 볼 수 있음
            
        stack.append((h, count))
    
    return result

# 입력 처리
n = int(sys.stdin.readline().strip())
heights = [int(sys.stdin.readline().strip()) for _ in range(n)]

# 결과 출력
print(count_visible_pairs(n, heights))
