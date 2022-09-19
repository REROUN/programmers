def solution(survey, choices):
    answer = ''

    ch = {
        1 : {'R' : 0, 'T' : 0},
        2 : {'C' : 0, 'F' : 0},
        3 : {'J' : 0, 'M' : 0},
        4 : {'A' : 0, 'N' : 0}
    }

    for idx, choice in enumerate(choices):
        if survey[idx] == "RT" or survey[idx] == "TR":
            if choice > 4:
                ch[1][survey[idx][1]] += choice - 4
            elif choice < 4:
                ch[1][survey[idx][0]] += 4 - choice
        if survey[idx] == "CF" or survey[idx] == "FC":
            if choice > 4:
                ch[2][survey[idx][1]] += choice - 4
            elif choice < 4:
                ch[2][survey[idx][0]] += 4 - choice
        if survey[idx] == "JM" or survey[idx] == "MJ":
            if choice > 4:
                ch[3][survey[idx][1]] += choice - 4
            elif choice < 4:
                ch[3][survey[idx][0]] += 4 - choice
        if survey[idx] == "AN" or survey[idx] == "NA":
            if choice > 4:
                ch[4][survey[idx][1]] += choice - 4
            elif choice < 4:
                ch[4][survey[idx][0]] += 4 - choice

    for i in ch:
        answer += max(ch[i], key=ch[i].get)
    
    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))