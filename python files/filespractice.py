'''reading the file'''
def reading():
    try:
        with open('python files/test.txt', 'r') as f:
            text = f.read()
        print(text)
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading the file.")
    with open('python files/test.txt') as f:
        text = f.read()
    print(text)

def writing_the_file():
    with open('python files/test.txt','w') as f:
        f.write('Ok now im adding the whole numers upto 1000')
        for i in range(1001):
            f.write(str(i)+'\n')
            
            
        
    with open('python files/test.txt','r') as f:
        text=f.read()

    print(text)    


def appendintoFiles():
    with open('python files/test.txt','w') as f:
        for i in range(21):
            f.write(str(i)+'\n')
            # this is overwritting the files and delete the previous data 
    with open('python files/test.txt','a') as f:
        # now im opening the same file and this time appending at the end
        for i in range(900):
            f.write(str(i)+'\n')
    # with open('python files/test.txt','r') as f:
    #     lines=list(f.read())
    #     print(lines)
    '''READ FILE LINE BY LINE'''
    with open('python files/test.txt','r') as f:
        for line in f:
            print(line)

'''OS IN PYTHON AND ITS DIFFERENT OPERATIONS'''


def os_module():
    import os
    if os.path.isfile('python files/test.txt'):
        print('file found')
    else:
        print('i think didnot find the file')
    if os.path.isdir('python files'):
        print('found the dir')
    # makiing a new dir
    try:
        os.mkdir('mydir')
    except FileExistsError:
        print('file with same name already exists')
    
    # deleting a file
    #  os.remove('del.txt')
    
    # delete the dir
    os.removedirs('mydir')

    # os.rename('del.txt','del_renamed.py')
    



os_module()