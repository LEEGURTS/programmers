// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/132265

import collections

def solution(topping):
    answer = 0
    secondSet = collections.defaultdict(int)
    firstSet = collections.defaultdict(int)
    
    for item in topping:
        secondSet[item]+=1
    
    for item in topping:
        firstSet[item]+=1
        secondSet[item]-=1
        if secondSet[item] == 0:
            del secondSet[item]
        if len(firstSet.keys()) == len(secondSet.keys()):
            answer+=1
    return answer