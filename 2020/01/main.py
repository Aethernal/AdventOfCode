import time
import functools


def step1(inputs, target):
    length = len(inputs)
    for i in range(length):
        if (target - inputs[i]) in inputs:
            return inputs[i], target - inputs[i]
    return None


def step2(inputs, target):
    length = len(inputs)
    for i in range(length):
        for j in range(i, length):
            if (target - inputs[i] - inputs[j]) in inputs:
                return inputs[i], inputs[j], target - inputs[i] - inputs[j]
    return None


def printResult(step, result):
    if result is not None:
        print('Step{} result is {} !'.format(
            step,
            functools.reduce(lambda x, y: x*y, result)
        ))
    else:
        print('Step{} failed !'.format(step))


if __name__ == "__main__":
    start = time.time()

    input = open('./01-input.txt', 'r')

    inputs = []
    for line in input.readlines():
        inputs.append(int(line))
    input.close()

    target = 2020

    printResult(1, step1(inputs, target))
    printResult(2, step2(inputs, target))

    print("time : {} ms".format((time.time() - start)*1000))
