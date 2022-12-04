def prepare_data(set_of_elves):
    elves = (set_of_elves.split(','))
    elf_1 = elves[0]
    elf_1_positions = elf_1.split('-')
    elf_1_starting = int(elf_1_positions[0])
    elf_1_ending = int(elf_1_positions[1])
    elf_2 = elves[1].replace('\n', '')
    elf_2_positions = elf_2.split('-')
    elf_2_starting = int(elf_2_positions[0])
    elf_2_ending = int(elf_2_positions[1])
    set_1 = set(range(elf_1_starting, elf_1_ending + 1))
    set_2 = set(range(elf_2_starting, elf_2_ending + 1))
    return set_1, set_2

def part1():
    counter = 0
    with open("C:/Users/nickb/source/repos/Personal/AdventOfCode/2022/data/day4.txt") as file:
        for set_of_elves in file:
            set_1, set_2 = prepare_data(set_of_elves)
            # check if set is fully contained and add to the counter if true
            if ((set_1.issubset(set_2)) or (set_1.issuperset(set_2))):
                counter += 1
    return counter

def part2():
    counter = 0
    with open("C:/Users/nickb/source/repos/Personal/AdventOfCode/2022/data/day4.txt") as file:
        for set_of_elves in file:
            set_1, set_2 = prepare_data(set_of_elves)
            # check if they overlap and add to the counter if true
            if set_1.intersection(set_2):
                counter += 1
    return counter
        
if __name__ == "__main__":
    print("part 1 answer:", part1())
    print("part 2 answer:", part2())