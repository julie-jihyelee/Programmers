def solution(my_string):
    new = []
    for i in my_string:
        if i in ['0','1','2','3','4','5','6','7','8','9'] :
            new.append(int(i))
    return sum(new)