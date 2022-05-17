def solution(a,b):
    # if a<=b:
    #     return sum(i for i in range(a,b+1))
    # else:
    #     return sum(i for i in range(b,a+1))

    if a>b:
        a,b=b,a
    
    return sum(range(a,b+1))



print(solution(5,3))
