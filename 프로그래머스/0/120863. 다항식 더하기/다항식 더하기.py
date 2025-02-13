def solution(polynomial):
    terms = polynomial.split(" + ")
    coefficient = 0 # 계수
    constant = 0 # 상수항
    
    for term in terms:
        #항에 x가 포함된 경우
        if "x" in term:
            num = term.replace("x","") # x제거
            coefficient += int(num) if num else 1 # else인 경우 계수가 1
        else:
            constant += int(term)
            
    result = []
    if coefficient:
        result.append(f"{coefficient}x" if coefficient != 1 else "x") # 계수가 1이면 x 반환
    
    if constant:
        result.append(str(constant))
    
    return (" + ".join(result))