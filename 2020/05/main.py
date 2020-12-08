import time

seatline_lower = "L"
seat_lower = "F"


def getID(row, column):
    return row * 8 + column


def readSeat(input, min=0, max=7, lower_char=seatline_lower, n=-1, n_start=-1):
    if(n is -1):
        n = len(input)
        n_start = n

    if(n != 1):
        if(input[n_start-n] is lower_char):
            max = (min + max + 1) // 2 - 1
        else:
            min = (min + max + 1) // 2
        n -= 1
        return readSeat(input, min, max, lower_char, n, n_start)
    else:
        if(input[n_start-n] is lower_char):
            return min
        else:
            return max


def step1(inputs):
    max = 0

    for seat in inputs:
        row = readSeat(seat[0:7], 0, 127, seat_lower)
        column = readSeat(seat[7:10])
        if(getID(row, column) > max):
            max = getID(row, column)

    return max


def step2(inputs):

    ids = []
    for seat in inputs:
        row = readSeat(seat[0:7], 0, 127, seat_lower)
        column = readSeat(seat[7:10])
        ids.append(getID(row, column))

    ids.sort()

    for n, id in enumerate(ids):
        if(ids[n+1]-ids[n] != 1):
            return ids[n] + 1


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
