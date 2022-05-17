def solution(numbers):
    answer=set()  #오름차순& 중복제거
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answer.add(numbers[i]+numbers[j])
    return list(sorted(answer))

numbers=[2,1,3,4,1]
print(solution(numbers))