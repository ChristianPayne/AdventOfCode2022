with open("input.txt", "r") as f:
 data = f.read()

def Check_For_Unique_Strings (length_of_string):
  for i, _ in enumerate(data):
    if(i < 4):
      continue
    check_indices = [i - step for step in range(length_of_string)]
    check_indices.reverse()
    check_set = set([data[i] for i in check_indices])
    if(len(check_set) == length_of_string):
      return i + 1

print("Marker found!", Check_For_Unique_Strings(4))
print("Message found!", Check_For_Unique_Strings(14))