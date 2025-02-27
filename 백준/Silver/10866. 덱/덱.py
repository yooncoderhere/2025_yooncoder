import sys
from collections import deque

def solution(commands):
    
    dq = deque()
    out = []
    
    for cmd in commands:
        
        #덱 앞에 추가
        if cmd.startswith("push_front"):
            _, x = cmd.split()
            dq.appendleft(int(x))
        #덱 뒤에 추가
        elif cmd.startswith("push_back"):
            _,x = cmd.split()
            dq.append(int(x))
            
        elif cmd == "pop_front":
            out.append(dq.popleft() if dq else -1)
        
        elif cmd == "pop_back":
            out.append(dq.pop() if dq else -1)
            
        elif cmd == "size":
            out.append(len(dq))
        
        elif cmd == "empty":
            out.append(1 if not dq else 0)
        #제거 하지 말고 출력
        elif cmd == "front":
            out.append(dq[0] if dq else -1)
            
        elif cmd == "back":
            out.append(dq[-1] if dq else -1)
    return out

input = sys.stdin.read
commands = input().split("\n")[:-1] #마지막 
output = solution(commands)
sys.stdout.write("\n".join(map(str,output))+ "\n")
