// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/118666

import collections

def solution(survey, choices):
    answer = ''
    score = collections.defaultdict(int)
    score["R"]=score["T"]=score["C"]=score["F"]=score["J"]=score["M"]=score["A"]=score["N"]=0
    for idx,item in enumerate(survey):
        score[item[1]] += choices[idx]-4
    if score["R"]>=score["T"]:
        answer+="R"
    else:
        answer+="T"
    if score["C"]>=score["F"]:
        answer+="C"
    else:
        answer+="F"
    if score["J"]>=score["M"]:
        answer+="J"
    else:
        answer+="M"
    if score["A"]>=score["N"]:
        answer+="A"
    else:
        answer+="N"
        
    return answer