def solution(arr):
    print(sum(arr))
    return sum([x for x in arr])/len(arr)

print(solution([1,2,3,4]))