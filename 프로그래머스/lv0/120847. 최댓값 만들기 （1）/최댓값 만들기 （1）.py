def solution(numbers):
    numbers.sort()
    result = numbers[-1]*numbers[-2]
    return result