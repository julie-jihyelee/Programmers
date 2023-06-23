def solution(my_strings, parts):
    new = ''
    for i in range(len(my_strings)):
        new += my_strings[i][parts[i][0]:parts[i][1]+1]
    return new