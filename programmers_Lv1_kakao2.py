def solution(id_list, report, k):
    answer = []

    report = list(set(report))

    u_name = {u : set() for u in id_list}
    cnt = {u : 0 for u in id_list}
    

    for re in report:
        r = re.split()
        u_name[r[0]].add(r[1])
        cnt[r[1]] += 1

    for id in id_list:
        result = 0
        for i in u_name[id]:
            if cnt[i] >= k:
                result += 1
        answer.append(result)

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
# print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
