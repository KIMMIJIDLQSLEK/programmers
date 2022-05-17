def solution(s):
    s=sorted(s,reverse=True)
    answer=''
    for i in s:
        answer+=i
    return answer
    # return "".join(sorted(s,reverse=True))

print(solution("Zbcdefg"))
    
