with open("input.txt", "r") as f:
 data = f.read()

elfs = data.split('\n\n')

max_calorie_elf = 0
for elf in elfs:
    elf_items = elf.split('\n')
    elf_items = map(lambda cal: int(cal), elf_items)
    elf_calories = sum(elf_items)
    if(max_calorie_elf < elf_calories):
      max_calorie_elf = elf_calories

print(max_calorie_elf)

