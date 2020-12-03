import time
import re


tree = "#"
free = "."


def calculateSlop(inputs, move):
    position = [0, 0]
    ymax = len(inputs)
    xmax = len(inputs[0]) - 1
    tree_encountered = 0

    while position[1] < ymax - 1:
        position[0] += move[0]
        position[1] += move[1]
        if(inputs[position[1]][position[0] % xmax] == tree):
            tree_encountered += 1

    return tree_encountered


def step1(inputs):
    return calculateSlop(inputs, [3, 1])


def step2(inputs):
    return (
        calculateSlop(inputs, [1, 1])
        * calculateSlop(inputs, [3, 1])
        * calculateSlop(inputs, [5, 1])
        * calculateSlop(inputs, [7, 1])
        * calculateSlop(inputs, [1, 2])
    )


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
