import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']


# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')
search_dir = 'C:\Code\GetIntoTech\PycharmProjects\Exercise10\*'

# TODO: Use the glob.glob() function to obtain the list of filenames
for file in glob.glob(search_dir):
    size = os.path.getsize(file)
    print(file, size)
print("_" * 50)
# TODO: use os.path.getsize to find each file's size

# TODO: Add a test to only display files that are not zero length

if file != 0:
    print(file)
else:
    print("file is 0")


# TODO: Remove the leading directory name(s) from each filename before you print it -
print(os.path.basename(file))
# using os.path.basename()

