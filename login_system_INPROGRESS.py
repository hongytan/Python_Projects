# Login system

with open("test.txt", 'r') as rf:
    characters = 10
    files_read = rf.read(characters)

    while len(files_read) > 0:
        print(files_read, end='$')
        files_read = rf.read(characters)
