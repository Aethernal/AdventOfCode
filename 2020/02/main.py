import time
import re


def step1(inputs):
    correct = 0

    regex = "\\b(?:[^{}\\s]*{}){{{},{}}}[^{}\\s]*\\b"

    for line in inputs:
        cmd = line.split(" ")
        min = cmd[0].split("-")[0]
        max = cmd[0].split("-")[1]
        char = cmd[1].split(":")[0]
        passwd = cmd[2]
        formated = regex.format(
            char,
            char,
            min,
            max,
            char
        )

        compiled = re.compile(formated)
        if(compiled.match(passwd)):
            correct += 1

    return correct


def step2(inputs):
    correct = 0

    for line in inputs:
        cmd = line.split(" ")
        min = int(cmd[0].split("-")[0])-1
        max = int(cmd[0].split("-")[1])-1
        char = cmd[1].split(":")[0]
        passwd = cmd[2]

        if(passwd[min] == char or passwd[max] == char) and passwd[min] != passwd[max]:
            correct += 1

    return correct


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
