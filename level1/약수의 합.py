#숫자의 약수의 리스트만들기
#숫자의 리스트 값 더하기
def solution(num):
    list=[]
    for i in range(1,num+1):
        mok=num//i
        if i>mok:
            break;
        if num%i==0:
            if mok!=i:
                list.append(i)
                list.append(mok)
            else:
                list.append(i)

    print(list)
    return sum(list)

num=int(input())
print(solution(num))