def solution(priorities, location):
    answer = 0
    count = 0

    dataset = dict(zip([i for i in range(len(priorities))], priorities))

    while True:
        if len(dataset) == 0:
            break
        printed = True

        first_key = list(dataset.keys())[0]
        temp = dataset.pop(first_key)

        for v in dataset.values():
            if temp < v:
                dataset[first_key] = temp
                printed = False
                break

        if printed:
            count = count + 1

            if first_key == location:
                break

    return count


res = solution([1, 1, 9, 1, 1, 1], 0)
print(res)
