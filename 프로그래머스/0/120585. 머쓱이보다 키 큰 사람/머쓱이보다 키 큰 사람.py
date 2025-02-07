def solution(array, height):
    count =0
    for i in range(len(array)):
        if array[i] > height:
            count +=1
    
    return count