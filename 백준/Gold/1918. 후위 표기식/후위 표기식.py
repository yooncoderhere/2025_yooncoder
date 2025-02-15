# 탐색의 순위가 있음

# 중위 표기식을 후위 표기식으로 변경

def solution(expression):

    precedence = {'+':1, '-':1, '*':2, '/':2 , '(':0} # 연산자 우선순위
    stack = [] # 연산자를 스택에 저장하고 꺼내는 방식으로
    result = [] #결과값 리스트

    for char in expression:
        if char.isalpha():
            result.append(char)
        
        elif char == '(':
            stack.append(char)
        
        elif char == ')': # 닫는 괄호가 나오면,
            #여는 괄호가 아니면, 
            while stack and stack [-1] != '(':
                result.append(stack.pop())
                
            if stack: # 여는 괄호 제거
                stack.pop()
            #그 외 연산자를 만나면
        else:
            while stack and precedence.get(stack[-1],-1) >= precedence.get(char,-1):
                #연산자 우선순위가 더 크다면,
                result.append(stack.pop())
                #아니라면,
            stack.append(char)
    while stack:
        result.append(stack.pop())
        #스택에 남아있는 연산자 모두 출력함
        
    return ''.join(result)

expression = input().strip()
print(solution(expression))
                
                