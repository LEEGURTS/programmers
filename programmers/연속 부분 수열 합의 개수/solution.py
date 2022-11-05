// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(elements):
    answer = []
    
    newElements = elements + elements
    for i in range(1,len(elements)+1):
        for j in range(len(elements)):
            answer.append(sum(newElements[j:j+i]))
    return len(set(answer))