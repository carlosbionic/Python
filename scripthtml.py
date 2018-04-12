# This script opens all files in all folders and checks for .html extension.
# If a .html file is found, a line of code 'str2' is added right after 'stri1'.

import os

print('Opening files to edit\n')
str1='<meta charset="UTF-8">\n'
str2='<meta name="viewport" content="width=device-width, initial-scale=1">\n'

for path, subdirs, files in os.walk("."):
 for name in files:
  if name.endswith(".html"):
   print (os.path.join(path, name)) # Prints the file to be edited.

   with open(os.path.join(path, name),'r') as in_file:
    buf = in_file.readlines()

   with open(os.path.join(path, name),'w') as out_file:
    for line in buf:
     if line == str1:
      line = line + str2
     out_file.write(line)

   out_file.close()
