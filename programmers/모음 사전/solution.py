// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    answer = 1
    wordSet = ["A",'E','I','O','U']
    for a in wordSet:
        if a == word:
            return answer
        answer+=1
        for b in wordSet:
            if a+b==word:
                return answer
            answer+=1
            for c in wordSet:
                if a+b+c==word:
                    return answer
                answer+=1
                for d in wordSet:
                    if a+b+c+d == word:
                        return answer
                    answer+=1
                    for e in wordSet:
                        if a+b+c+d+e == word:
                            return answer
                        answer+=1
    return answer