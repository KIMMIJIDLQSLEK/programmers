def first_last(new):
    if new[0]=='.':
        new=new[1:]
    elif new[len(new)-1]=='.':
        new=new[:len(new)-1]
    return new

def solution(new_id):

    use=['0','1','2','3','4','5','6','7','8','9','-','_','.']
    new=''
    #규칙1,2,3
    for i in range(len(new_id)):
        result=ord(new_id[i])
        if new_id[i]>='A' and new_id[i]<='Z':
            new+=chr(ord(new_id[i])+32)

        if new_id[i] in use or (new_id[i]>='a' and new_id[i]<='z'):
            new+=new_id[i]

        new=new.replace('..','.')

    #규칙4
    new=first_last(new)

    #규칙5
    if len(new)==0:
        new+='a'

    #규칙6
    if len(new)>=16:
        new=new[:15]
    new=first_last(new)

    #규칙7
    new_length=len(new)
    i=new[new_length-1]
    if new_length<=2:
        while(len(new)<3):
            new+=i

    return new

new_id="...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))