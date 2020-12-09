import time
import itertools


def step1(inputs):

    offset = 25
    for index, v in enumerate(inputs[25:]):
        keys = inputs[index:offset+index]

        combinations = sorted(list(dict.fromkeys([
            int(tuple[0]) + int(tuple[1])
            for tuple in list(itertools.combinations(keys, 2))
        ])))

        if int(v) not in combinations:
            return int(v)

    return None


def step2(inputs):
    target = 373803594

    for index, v in enumerate(inputs):
        count = 0
        added = []
        for i2, v2 in enumerate(inputs[index::]):
            count += int(v2)
            added.append(int(v2))
            if count == target:
                return min(added) + max(added)
            elif count > target:
                break

    return None


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
        inputs.append(line.strip())
    input.close()

    printResult(1, inputs)
    printResult(2, inputs)

    print("time : {} ms".format((time.time() - start)*1000))
