from collections import deque

def solution(progresses, speeds):
    days = deque([(100-p+s-1) // s for p ,s in zip(progresses, speeds)])
    result = []
    
    while days:
        deploy_day = days.popleft()
        count = 1
        
        while days and days[0] <= deploy_day:
            days.popleft()
            count +=1
            
        result.append(count)
    
    return result