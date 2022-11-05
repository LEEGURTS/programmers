// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/131127

import collections

def solution(want, number, discount):
    answer = 0
    length = sum(number)
    wantLength = len(number)
    discountLength = len(discount)
    counter = collections.Counter(discount[0:length])
    for i in range(len(discount)-length+1):   
        flag = True
        for j in range(wantLength):
            if counter[want[j]] != number[j]:
                flag=False
                break;
        if flag == True:
            answer+=1
        if i != discountLength-length:
            counter[discount[i]]-=1
            counter[discount[i+length]]+=1
    return answer