// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/134239

def solution(k, ranges):
    answer = []
    array = [k]
    while k != 1:
        if k % 2 == 0:
            k/=2
            array.append(k)
        else:
            k = 1+k*3
            array.append(k)
    size = []
    for i in range(1,len(array)):
        size.append((array[i-1]+array[i])/2)
        
    sizeLength = len(size)
    for item in ranges:
        endPos = sizeLength + item[1]
        if item[0] > endPos:
            answer.append(-1)
        else:
            answer.append(sum(size[item[0]:endPos]))
    return answer