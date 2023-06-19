def solution(array, height):
    tall = []
    for i in range(len(array)) :
        if array[i] > height :
            tall.append(array[i])

    return len(tall)