def solution(myString, pat):
    newString=''
    for i in range(len(myString)):
        if myString[i] == 'A' :
            newString += 'B'
        else :
            newString += 'A'
            
    if pat in newString:
        result = 1
    else :
        result = 0
        
    return result