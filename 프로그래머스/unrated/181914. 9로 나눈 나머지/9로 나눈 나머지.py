def solution(number):
    
    add = 0
    for i in range(len(number)):
        add += int(number[i])
        if int(number)%9 == add%9 :
            return int(number)%9