def solution(today, terms, privacies):
    answer = []

    today = list(map(int, today.split('.')))
    terms = {i.split(' ')[0] : int(i.split(' ')[1]) for i in set(terms)}

    for idx, privacie in enumerate(privacies):
        privacie = privacie.split(' ')
        t = privacie[-1]
        privacie = list(map(int, privacie[0].split('.')))

        y = privacie[0]
        m = privacie[1]
        d = privacie[2]

        if terms[t] > 12:
            y += terms[t] // 12
            m += terms[t] % 12
            d = privacie[2] - 1
        else:
            m = privacie[1] + terms[t]
            d = privacie[2] - 1

        if m > 12:
            y += m // 12
            m = m % 12
        
        if d < 1:
            d = 28
            m -= 1
            if m < 1:
                m = 12
                y -= 1

        print(y, m, d)

        if  today[0] < y:
            continue
        elif today[0] == y:
            if today[1] < m:
                continue
            elif today[1] == m:
                if today[2] > d:
                    answer.append(idx + 1)
                else:
                    continue
            else:
                answer.append(idx + 1)
        else:
            answer.append(idx + 1)
        
    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
# print(solution("2020.01.01", ["Z 100", "D 23"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))