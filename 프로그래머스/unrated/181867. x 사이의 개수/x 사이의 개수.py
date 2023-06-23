def solution(myString):
    new = []
    a = myString.split('x')
    for i in range(len(a)):
        new.append(len(a[i]))
    return new