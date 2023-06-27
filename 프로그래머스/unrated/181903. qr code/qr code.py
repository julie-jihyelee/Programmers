def solution(q, r, code):
    new = ''
    for i, s in enumerate(code):
        if i%q == r :
            new += s
    return new
        