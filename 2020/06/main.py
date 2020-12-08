import time


def step1(inputs):
    groups = []
    current = {}
    for line in inputs:

        if(line == "\n"):
            groups.append(current)
            current = {}
        else:
            for c in line.strip():
                current[c] = 1

    groups.append(current)

    total = 0
    for group in groups:

        total += len(group)
    return total


def step2(inputs):
    groups = []
    current = {}
    people_in_group = 0
    for line in inputs:
        if(line == "\n"):
            current["people"] = people_in_group
            groups.append(current)
            current = {}
            people_in_group = 0
        else:
            people_in_group += 1
            for c in line.strip():
                if c in current.keys():
                    current[c] = current[c] + 1
                else:
                    current[c] = 1

    current["people"] = people_in_group
    groups.append(current)

    total = 0
    for group in groups:
        print(group)
        print("---")
        for key in group.keys():
            if(key != "people" and group[key] == group["people"]):
                total += 1
        print(total)
    return total


steps = [step1, step2]


def printResult(step, inputs):
    if inputs is not None:
        print('Step{} result is {} !'.format(
            step,
            steps[step-1](inputs)
        ))
    else:
        print('Step{} failed !'.format(step))


if __name__ == "__main__":
    start = time.time()

    input = open('./input.txt', 'r')

    inputs = []
    for line in input.readlines():
        inputs.append(line)
    input.close()

    printResult(1, inputs)
    printResult(2, inputs)

    print("time : {} ms".format((time.time() - start)*1000))
