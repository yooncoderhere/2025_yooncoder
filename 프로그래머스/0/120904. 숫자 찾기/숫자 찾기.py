def solution(num, k):
    str_num = str(num) #숫자를 문자열로 전환
    str_k = str(k)
    
    if str_k in str_num:
        return str_num.index(str_k) +1 # 1-based
    return -1 # 없으면 -1 반환