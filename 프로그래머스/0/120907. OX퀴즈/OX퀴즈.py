def solution(quiz):
    result = [] # 빈 배열
    for q in quiz:
        X,op, Y, _, Z = q.split() # 문자열 분해
        
        if op == '+':
            answer = int(X)+int(Y)
            
        else: # 뺄셈
            answer = int(X)-int(Y)
            
        result.append("O" if answer == int(Z) else "X") # 
            
    return result