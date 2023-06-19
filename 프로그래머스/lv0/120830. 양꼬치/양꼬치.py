def solution(n, k):
    money = 0
    if n < 10 :
        money = (n*12000)+(k*2000) 
    elif n//10 >= 1 :
        money = (n*12000)+((k-(n//10))*2000)
        
    return money