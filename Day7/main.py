with open("input.txt", "r") as f:
 data = f.read().split('\n')

# A class for a file.
class File:
  name = ''
  file_size = 0

# A class for directories.
class Dir:
  name = ''
  contents = []

  def GetDirSize(self, cutoff: int):
    total_size = 0
    for item in self.contents:
      if type(item) == Dir:
        # Add up all the children that are > 100,000. If a dir has more, dont count it up keep the size of the children under 100,000
        total_size += item.GetDirSize(cutoff)
      else:
        total_size += item.file_size

    print(f"Dir {self.name} is of size {total_size}")
    if(total_size <= cutoff):
      return total_size
    else:
      return 0

def CreateItem(input: str):
  input_list = input.split(' ')
  if input_list[0] == 'dir':
    dir = Dir()
    dir.name = input_list[1]
    dir.contents = []
    print('Created Dir', dir.name)
    return dir
  else:
    file = File()
    file.file_size = int(input_list[0])
    file.name = input_list[1]
    return file

# Keep track of dir in list form.
current_directory_url = []

root_dir = Dir()
root_dir.name = '/'

# Have a function for finding a dir with a specific name.
def GetDir(directory: Dir, dir_name: str) -> Dir:
  # print(f"Checking {directory.name} for {dir_name}")
  if directory.name == dir_name:
    return directory

  for item in directory.contents:
    if type(item) == Dir:
      if item.name == dir_name:
        print("Found dir", item.name, item.contents)
        return item

      dir = GetDir(item, dir_name)
      if dir != None:
        return dir
  
  # print("didnt find anything")



def ParseInput():
  global listing_directory
  listing_directory = False
  directory_items = []

  for row in data:
    print('START:',row)
    if row.startswith('$'):
      if(listing_directory):
        print("/".join(current_directory_url))
        dir = GetDir(root_dir, current_directory_url[-1])
        print(type(dir))
        if dir != None and len(dir.contents) == 0:
          dir.contents = directory_items
          print('Set URL contents', current_directory_url)

        directory_items = []
        listing_directory = False
      command = row.split(' ')
      # print("This is a command", command)
      if command[1] == 'cd':
        if command[2] == '..':
          current_directory_url.pop()
        else:
          current_directory_url.append(command[2])
        print('CD:', "/".join(current_directory_url))
      if command[1] == 'ls':
        listing_directory = True
    else:
      if(listing_directory):
        item = CreateItem(row)
        directory_items.append(item)
      # print("We created an item", item)
    # print('END',row)

ParseInput()

# while True:
#   command = input("Enter command...")
#   if(command == 'ls'):
#     dir = FindDir(current_directory_url[-1])
#     map(lambda d: print(d.name), dir.contents)

print(root_dir.GetDirSize(100000))

# 718860 is too low