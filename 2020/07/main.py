import time

delimiter_contain = "bags contain"
no_other_bag = "no other bags"
count_target = "shiny gold"


def search_bag(bag_dict, targets, previous=[], n=0):
    found = []

    if(not targets):
        return found

    for target in targets:
        if target in bag_dict:
            for bag in bag_dict[target].keys():
                if bag not in previous:
                    previous.append(bag)
                    found.append(bag)

    if n > 0:
        return targets + search_bag(bag_dict, found, previous, n + 1)
    else:
        return search_bag(bag_dict, found, previous, 1)


def step1(inputs):

    bag_dict = {}

    for bag_rule in inputs:

        first_split = bag_rule.replace(".", "").strip().split(delimiter_contain)
        bag_ruled = first_split[0].strip()

        if(first_split[1].strip() != no_other_bag):
            bags = first_split[1].strip().split(",")
            for bag in bags:
                bag_data = bag.strip().split(" ")  # 0 count, 1+ name
                bag_name = " ".join(bag_data[1::]).replace("bags", "").replace("bag", "").strip()
                bag_count = int(bag_data[0])
                if(bag_dict.get(bag_name) is None):
                    bag_dict[bag_name] = {}
                bag_dict[bag_name][bag_ruled] = bag_count

    bags = search_bag(bag_dict, [count_target])
    return len(bags)


def count_bag(bag_dict, target, n=0):
    count = 0

    margin = ""
    for x in range(n):
        margin += "-|"

    if bag_dict.get(target) is not None:

        for k, v in bag_dict[target].items():
            if bag_dict.get(k) is not None:
                bag_count = count_bag(bag_dict, k, n+1)
                print(f"{margin} bag {target} contain {v} {k} bag => {bag_count} bag => {v * bag_count} ")
                count += v * bag_count + v
            else:
                count += v
        return count
    else:
        return 1


def step2(inputs):

    bag_dict = {}

    for bag_rule in inputs:

        first_split = bag_rule.replace(".", "").strip().split(delimiter_contain)
        bag_ruled = first_split[0].strip()

        if(first_split[1].strip() != no_other_bag):
            bags = first_split[1].strip().split(",")
            for bag in bags:
                bag_data = bag.strip().split(" ")  # 0 count, 1+ name
                bag_name = " ".join(bag_data[1::]).replace("bags", "").replace("bag", "").strip()
                bag_count = int(bag_data[0])
                if(bag_dict.get(bag_ruled) is None):
                    bag_dict[bag_ruled] = {}
                bag_dict[bag_ruled][bag_name] = bag_count

    count = count_bag(bag_dict, "shiny gold")
    return count


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
