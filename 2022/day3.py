from string import ascii_lowercase
from string import ascii_uppercase

sorted_lower_ascii = sorted(set(ascii_lowercase))
sorted_upper_ascii = sorted(set(ascii_uppercase))
sorted_ascii_letters = [*sorted_lower_ascii, *sorted_upper_ascii]

def part1():
    sum_of_priorities = 0

    with open("C:/Users/nickb/source/repos/Personal/AdventOfCode/2022/data/day3.txt") as file:
        for line in file:
            first_compartment = line[:len(line)//2]
            second_compartment = line[len(line)//2:]

            has_match = False
            for item_a in first_compartment:
                    if item_a not in second_compartment:
                        continue
                    else:
                        sum_of_priorities += sorted_ascii_letters.index(item_a) + 1
                        has_match = True

                    if has_match == True:
                        break
    return sum_of_priorities


def part2():
    elves = []
    sum_of_priorities = 0
    elf_badges = []

    with open("C:/Users/nickb/source/repos/Personal/AdventOfCode/2022/data/day3.txt") as file:
        for line in file:
            elf_sack = line.replace('\n', '')
            elves.append(elf_sack)

    elf_groups = [elves[n:n+3] for n in range(0, len(elves), 3)]

    for elf_group in elf_groups:
        for elf_sack in elf_group:
            for item in elf_sack:
                if item in elf_group[1]:
                    if item in elf_group[2]:
                        elf_badges.append(item)
                        break
            break
                
    for badges in elf_badges:
        sum_of_priorities += sorted_ascii_letters.index(badges) + 1
                   
    return sum_of_priorities
        
if __name__ == "__main__":
    print("answer for part 1: ", part1())
    print("answer for part 2: ", part2())