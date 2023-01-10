// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/42883

import collections

def solution(number, k):
    answer = []
    for num in number:
        if not answer:
            answer.append(num)
            continue
        if k > 0 and answer[-1] < num:
            while k > 0 and answer and answer[-1] < num:
                answer.pop()
                k-=1
            answer.append(num)
        else:
            answer.append(num)
        
    while k>0:
        answer.remove(min(answer))
        k-=1
    return "".join(answer)