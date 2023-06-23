def solution(n):
    
    result = [n]
    for i in range(n):
        if result[i] == 1 :
            break
        elif result[i]%2 == 0 :
            result.append(result[i]/2)
        elif result[i]%2 != 0 :
            result.append(3*result[i]+1)
        
    return result