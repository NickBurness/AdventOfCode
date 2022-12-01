elf_calories_list = []
elf_calories = 0

with open("C:/Users/NBURNESS/source/repos/side/AdventOfCode/2022/data/day1.txt") as file:
    for line in file:
        if (line.strip() == ""):
            elf_calories_list.append(elf_calories)
            elf_calories = 0
        else:
            elf_calories += int(line)


max_calories = max(elf_calories_list)
print("total calories of top elf:", max_calories)


total_calories = 0
top3 = sorted(elf_calories_list, reverse=True)[:3]
for elf in top3:
    total_calories += elf
print("total calories of top 3 elves:", total_calories)