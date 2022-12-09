

THRESHOLD = 100000
FILESYSTEM = 70000000
FREESPACE_NEEDED = 30000000

class Dir:
    def __init__(self, name=None, parentdir=None):
        self.name = name
        self.files = []
        self.subdirs = []
        self.parentdir = parentdir


    def size(self)->int:
        '''
        Get the size of all files in this dir and all subdirs
        '''
        size = 0
        for file in self.files:
            size += file['size']
        for dir in self.subdirs:
            size += dir.size()
        return size

    
    def flatten_dirs(self):
        '''
        Flatten all the subdirectories in the tree into a an array for easy iteration
        '''
        dirs = []
        dirs.append(self)
        dirs.extend(self.subdirs)
        for dir in self.subdirs:
            dirs.extend(dir.flatten_dirs())
        return dirs
    
    def __str__(self):
        '''
        Dirty string representation of the directory
        '''
        result = f'- {self.name} (dir)'
        for subdir in self.subdirs:
            result = result + str(subdir)
        for file in self.files:
            result = result + f'\n - {file["name"]} ({file["size"]})'
        
        return result

def walk(lines):
    root = Dir(name="/")
    current_dir = root
    for line in lines:
        if line.startswith("$ cd /"):
            pass
        elif line.startswith("$ cd .."):
            current_dir = current_dir.parentdir
        elif line.startswith("$ cd "):
            newdir = Dir(name=line.split(" ")[2], parentdir=current_dir)
            current_dir.subdirs.append(newdir)
            current_dir = newdir
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir "):
            #current_dir.subdirs.append(line.split(" ")[1])
            pass
        else:
            current_dir.files.append({"name":line.split(" ")[1], "size": int(line.split(" ")[0])})
    return root


with open('/workspaces/adventofcode2022/day7/input', 'r') as f:
    lines = f.readlines()

result = walk(lines)

total_size = 0

all_dirs_size = []
unique_dirs = list(dict.fromkeys(result.flatten_dirs()))
for dir in unique_dirs:
    print(f'{dir.name} - {dir.size()}')
    all_dirs_size.append(dir.size())
    if dir.size() <= 100000:
        total_size = total_size + dir.size()
    

all_dirs_size.sort()

print(f'Total size of dirs < {THRESHOLD} : {total_size}')
print(f'Total size of root dir is: {result.size()}')
needed_space = FREESPACE_NEEDED - (FILESYSTEM - result.size())
print(f'Total size of space needed to free up is: {needed_space}')
for dir_size in all_dirs_size:
    if dir_size > needed_space:
        print(dir_size)
        break