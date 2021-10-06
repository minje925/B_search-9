n = int(input())
alist = list(map(int, input().split()))
answer = [0]
str = ''

for i in range(len(alist)):
    if alist[0] > answer[-1] and alist[-1] > answer[-1]:
        if alist[0] < alist[-1]:
            answer.append(alist[0])
            alist.pop(0)
            str+='L'
        else:
            answer.append(alist[-1])
            alist.pop()
            str+='R'
    elif alist[0] > answer[-1]:
        answer.append(alist[0])
        alist.pop(0)
        str+='L'
    elif alist[-1] > answer[-1]:
        answer.append(alist[-1])
        alist.pop()
        str+='R'
answer = answer[1:]
print(len(answer))
print(str)
