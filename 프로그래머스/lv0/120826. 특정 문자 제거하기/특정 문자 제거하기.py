def solution(my_string, letter):
    new = ""
    for i in my_string :
        if i != letter :
            new += i
    return new