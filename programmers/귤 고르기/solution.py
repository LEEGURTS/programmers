// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/138476

import collections

def solution(k, tangerine):
    answer = 0
    counted = collections.Counter(tangerine).most_common()
    while k>0:
        k-=counted[answer][1]
        answer+=1
    return answer