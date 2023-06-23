def solution(myString):
    myString = myString.split('x')
    new =[]
    for i in range(len(myString)):
        if myString[i] != '':
            new.append(myString[i])
    new.sort()
    return new
    