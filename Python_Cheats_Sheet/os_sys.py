"""
os and sys built-in modules
"""


# os library
import os

# check if file or folder exists using .exists()
os.path.exists("/filepath")

if os.path.exists("./new_folder/"):
  print("file exists")

else:
  # create folder using os.madedir()
  os.makedirs("./new_folder/")


print("")

# list folder/dir contents
os.listdir()

# split filename from it's extension

split_file = os.path.splitext("./Python_Cheat_Sheet.py")

print(f"This is the file name: {split_file[0]}")

print("This is the file extension: %s " % split_file[1])


# sys library
import sys

sys.argv
# sys.argv allows user to include argument when running scripts.
# Command line arguments are always strings, so if we decided to
# use ints as args, then we should convert(cast) to int() first.

script_name = sys.argv[0] # => Python script (file) name.
first_argument = sys.argv[1]
second_argument = sys.argv[2]

# run a Python script with args:
# $ script.py first_argument second_argument


if len(sys.argv) > 1:
    print(f"Hello {second_argument.capitalize()}!")


# iterate over all args
for arg in sys.argv:
    print(arg)
    
