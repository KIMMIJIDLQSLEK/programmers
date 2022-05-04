def solution(s):
    list=['1','2','3','4','5','6','7','8','9','0']
    for i in s:
        if not i in list:
            return False
    return len(s) in (4,6)

input=input()
print(solution(input))


# def solution(s):
#     if s.isdigit() and len(s) in (4,6):
#         return True
#     return False

# input=input()
# print(solution(input))

