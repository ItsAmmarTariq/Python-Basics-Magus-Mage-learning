try:
    with open('python files/test.txt', 'r') as f:
        text = f.read()
    print(text)
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("Error reading the file.")
