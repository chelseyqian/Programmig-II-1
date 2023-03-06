lines = ["Hello, ", "world", "!"]

# File write mode 'w' is overwrite by default
# Use 'a' for append
with open("data/myfile.txt", 'w') as f:
  # Write data to a file
  f.write("Hi \n")
  f.writelines(lines)
  # or, for line in lines: file.wiite(line)

with open("data/myfile.txt", 'r') as f:
  # Reading from a file
  print(f.read())