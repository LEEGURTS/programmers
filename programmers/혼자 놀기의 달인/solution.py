// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/131130

def solution(cards):
    scores = []
    if not cards:
        return 0
    checked = [0 for _ in range(len(cards))]
    for i in range(len(cards)):
        if checked[i]:
            continue;
        count = 0
        start = cards[i] - 1
        while not checked[start]:
            count += 1
            checked[start] = 1
            start = cards[start] - 1
        scores.append(count)
    scores.sort(reverse=True)
    if len(scores) < 2:
        return 0
    return scores[0] * scores[1]
