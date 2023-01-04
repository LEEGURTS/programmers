// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/42885

import collections

def solution(people, limit):
    answer = 0
    people.sort()
    queue = collections.deque(people)

    while queue:
        heavy = queue.pop()
        if queue:
            if queue[0] + heavy <= limit:
                queue.popleft()
        answer+=1
        
    return answer