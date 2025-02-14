def solution(my_string):
    total_sum = 0  # 합을 저장할 변수
    current_num = ''  # 현재까지 읽은 숫자 (문자열)
    
    for char in my_string:
        if char.isdigit():  # 숫자인 경우
            current_num += char  # 숫자를 이어붙임
        else:
            if current_num:  # 숫자 끝났다면 # 이 부분이 핵심적임
                total_sum += int(current_num)  # 합산
                current_num = ''  # current_num 초기화

    # 마지막에 남아있는 숫자도 합산
    if current_num:
        total_sum += int(current_num)

    return total_sum
