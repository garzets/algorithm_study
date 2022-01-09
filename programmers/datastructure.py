def solution(progresses, speeds):
    answer = list()

    while True:
        if len(progresses) == 0:
            break;

        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]

        count = 0
        while True:
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                count = count + 1
                if len(progresses) == 0:
                    break;
            else:
                break;

        if count > 0:
            answer.append(count)
    return answer


solution([93, 30, 55], [1, 30, 5])
