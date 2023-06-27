def solution(my_string):
    result=[]
    
    for char in list(my_string):
        if char.isnumeric():
            result.append(int(char))
    
    result.sort()
    
    return result
