def solution(arr, intervals):
    list1 = arr[intervals[0][0]:intervals[0][1]+1]
    list2 = arr[intervals[1][0]:intervals[1][1]+1]
    result = list1 + list2
    return result