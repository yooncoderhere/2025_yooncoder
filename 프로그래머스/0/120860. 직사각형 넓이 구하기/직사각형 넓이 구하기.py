def solution(dots):
    
    x_values = [dot[0] for dot in dots]
    y_values = [dot[1] for dot in dots]
    
    width = max(x_values) - min(x_values)
    height = max(y_values) - min(y_values)
    
    return width * height 