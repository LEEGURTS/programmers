// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/42862?itm_content=course14743#

def solution(n, lost, reserve):
    answer = 0
    checkArray = [0 for i in range(n+1)]
    for los in lost:
        checkArray[los] -= 1
    for res in reserve:
        if checkArray[res] == -1:
            answer+=1
        checkArray[res] += 1
    print(checkArray)
    for i in range(1,n+1):
        if checkArray[i] == 1 and checkArray[i-1] == -1:
            answer+=1
            checkArray[i]=0
            checkArray[i-1]=0
        elif i < n and checkArray[i] == 1 and checkArray[i+1] == -1:
            answer+=1
            checkArray[i]=0
            checkArray[i+1]=0

    return n + answer - len(lost)