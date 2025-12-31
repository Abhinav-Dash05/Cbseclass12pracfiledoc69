filename = input("Enter file name: ")

try:
    file = open(filename, "r")
    print("Reading file line by line: ")

    for line in file:
        line = line.strip()
        print(line)

    file.close()

except FileNotFoundError:
    print("File not found. Please check the file name.")