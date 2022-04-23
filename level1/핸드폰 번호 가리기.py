def solution(phone_number):
    answer='*'*(len(phone_number)-4)+phone_number[len(phone_number)-4:]
    return answer

phone_number=input()
print(solution(phone_number))