# prompt for a file name, open file, remove spaces and print it on uppercase
file_name = input("Enter file name: ")
fh = open(file_name)
for letter in fh:
    ly = letter.rstrip()
    print(ly.upper())
