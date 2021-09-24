"""
glob built-in module

 - In Python, the glob module is used to retrieve files/pathnames matching a 
   specified pattern.
 - unlike os.listdir(), glob() can customize files/folder search using wild
   cards like *.*
"""

import glob

# using wild card * to retreive all files
print("using wild card *")
for info in glob.glob("../Python_Cheats_Sheet/*"):
  print(info, end="\n\n")

print("")

for file in glob.glob("../Python_Cheats_Sheet/op*.py"):
  print(file)
  print(type(file))

