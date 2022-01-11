import os,sys

try:
    file = sys.argv[1]
except:
    print("You need to specify the file")
else:
    if file is None:
        print("You need to specify the file")
        sys.quit()

with open(file, 'r') as f:
    content = f.readlines()

unique_lines = []
for line in content:
    if line not in unique_lines:
        unique_lines.append(line)

with open(file, 'w') as f:
    f.write("".join(unique_lines))
