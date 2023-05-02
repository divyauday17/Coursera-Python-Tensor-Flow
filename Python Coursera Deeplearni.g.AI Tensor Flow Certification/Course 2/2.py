filename = input("Enter file name: ")
try:
    file = open(filename, 'r')
    for line in file:
        print(line.upper().rstrip())
    file.close()
except FileNotFoundError:
    print("File not found.")