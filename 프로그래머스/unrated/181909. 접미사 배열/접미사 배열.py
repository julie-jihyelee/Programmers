def solution(my_string):
    new =[]
    for i in range(len(my_string)):
        new.append(my_string[i:])
    new.sort()
    return new