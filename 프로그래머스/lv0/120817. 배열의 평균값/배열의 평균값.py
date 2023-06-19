def solution(numbers):
    add =0
    for i in range(len(numbers)) :
        add += numbers[i]
    
    result = add/len(numbers)
    return result
    