def solution(n):
    if n%2==0:
        return "수박"*(n//2)
    else:
        return "수박"*(n//2)+"수"


input=int(input())
result=solution(input)
print(result)