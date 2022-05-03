

# def solution(n):
#     sosu_count=0
#     for num in range(2,n+1):  #1은 소수에 포함이 안되므로
#         sosu=0
#         for i in range(2,num//2+1):  #1과 자기자신을 뺀 나머지가 약수일경우 소수아님
#             if num%i==0:
#                 sosu=1
#                 break;
            
#         if sosu==0:  #소수일경우
#             sosu_count+=1
    
#     return sosu_count

#제곱근구하여 정수의 값의 배수를 지워나가는 방법: 에라스코테네스의 체


def solution(n):
    sosu=set(range(2,n+1))  #2~n까지의 수를 모두 소수라고 가정한다.

    for i in range(2,n+1): #2부터 n까지의 수중에서 소수를 찾을것이다.
        if i in sosu:
            sosu-=set(range(i*2,n+1,i))


    return len(sosu)

n=int(input())
print(solution(n))
