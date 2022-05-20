'''
최고순위: win_nums와 일치한 횟수+0인 횟수
최저순위: win_nums와 일치한 횟수
횟수에 맞는 로또 당첨번호 출력

'''
def rank(num):
    if num==6:
        return 1
    elif num==5:
        return 2
    elif num==4:
        return 3
    elif num==3:
        return 4
    elif num==2:
        return 5
    else:
        return 6

def solution(lottos,win_nums):
    ans_cnt=0
    zero_cnt=0
    for num in lottos:
        if num in win_nums:
            ans_cnt+=1
        if num==0:
            zero_cnt+=1
    
    return [rank(zero_cnt+ans_cnt),rank(ans_cnt)]

lottos=[45, 4, 35, 20, 3, 9]
win_nums=[20, 9, 3, 45, 4, 35]
print(solution(lottos,win_nums))
