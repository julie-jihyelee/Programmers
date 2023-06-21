def solution(intStrs, k, s, l):
    result = []
    for i in range(len(intStrs)):
        string = intStrs[i]
        num = int(string[s:s+l])
        if num > k :
            result.append(num)
    return result