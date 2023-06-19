def solution(n):
    new = []
    n = str(n)
    for i in range(len(n)):
        a = int(n[i])
        new.append(a)
    return sum(new)