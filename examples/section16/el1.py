import glob

myfiles = glob.glob('exercises/*.txt')

for filepath in myfiles:
    print(filepath)
    with open(filepath, 'r') as file:
        print(file.read())
