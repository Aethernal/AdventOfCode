import time
import re

ecl_value = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def validateECL(value):
    return value in ecl_value


def validatePID(value):
    return re.compile("^[0-9]{9}$").match(value)


def validateEYR(value):
    return int(value) <= 2030 and int(value) >= 2020


def validateHCL(value):
    return re.compile("#[0-9a-f]{6}").match(value) is not None


def validateBYR(value):
    return int(value) <= 2002 and int(value) >= 1920


def validateIYR(value):
    return int(value) <= 2020 and int(value) >= 2010


def validateHGT(value):
    if(value.endswith("cm")):
        if(int(value.split("cm")[0]) >= 150 and int(value.split("cm")[0]) <= 193):
            return True
    elif(value.endswith("in")):
        if(int(value.split("in")[0]) >= 59 and int(value.split("in")[0]) <= 76):
            return True
    return False


required_params = {
    "ecl": validateECL,
    "pid": validatePID,
    "eyr": validateEYR,
    "hcl": validateHCL,
    "byr": validateBYR,
    "iyr": validateIYR,
    "hgt": validateHGT
}


def parsePassports(inputs):
    passports = []
    current = {}

    for line in inputs:
        if(line == "\n"):
            passports.append(current)
            current = {}
            continue
        for param in line.split(" "):
            current.update({param.split(":")[0]: param.split(":")[1].strip()})

    passports.append(current)
    return passports


def step1(inputs):
    valid = 0
    passports = parsePassports(inputs)

    for passport in passports:
        if (all(param in passport.keys() for param in required_params.keys())):
            valid += 1
    return valid


def step2(inputs):
    valid = 0
    passports = parsePassports(inputs)

    for passport in passports:
        if (all(param in passport.keys() and required_params[param](passport[param]) for param in required_params.keys())):
            valid += 1
    return valid


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
