# define problem
# --------------

# find the elf carrying the most calories
# each elf is seperated by a new line in the input file
# each elf could have one or more food items with calories

# implementation
# --------------

# create an empty list to hold each elf calories
elf_calories_list = []
# create an elf calories counter starting at 0
elf_calories = 0
# loop the list
with open("C:/Users/NBURNESS/source/repos/side/AdventOfCode/2022/data/day1.txt") as file:
    for line in file:
        # if the line is empty, it is a new elf, add the calories for that elf to the empty list
        if (line.strip() == ""):
            elf_calories_list.append(elf_calories)
            # reset the elf calorie counter ready for the next elf
            elf_calories = 0
        else:
            # read the files string as an integer and add it to the existing counter
            elf_calories += int(line)

# get the max number of calories in the new list
max_calories = max(elf_calories_list)
print("total calories of top elf:", max_calories)

# set total_calories to 0
total_calories = 0
# sort the list and get only the top 3
top3 = sorted(elf_calories_list, reverse=True)[:3]
# add each of the top 3 together
for elf in top3:
    total_calories += elf
print("total calories of top 3 elves:", total_calories)
