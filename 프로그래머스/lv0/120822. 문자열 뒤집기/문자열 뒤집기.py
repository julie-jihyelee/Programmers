def solution(my_string):
    new = []
    for i in range(len(my_string)):
        new.insert(0, my_string[i])
    return ''.join(new)