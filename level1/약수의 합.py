#약수: 나머지가 0일경우
def solution(num):
    sum=0
    for i in range(1,num+1):
        if num%i==0:
            sum+=i
    return sum

num=int(input())
print(solution(num))