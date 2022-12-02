with open("input.txt", "r") as f:
 data = f.read()

elves = [sum([int(item) for item in elf.split('\n')]) for elf in data.split('\n\n')]
elves.sort()
elves.reverse()

print(sum(elves[0:3]))