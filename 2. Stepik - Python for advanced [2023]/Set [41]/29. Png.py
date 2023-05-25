# Using a set generator, augment the above code so that it selects unique names of files 
# with the extension .png from the list of files, regardless of the case of names and extensions. 
# Output the file names together with their extensions, all on one line, in lowercase, in alphabetical order, 
# separated by a space.

# Note. If the list of files contained the following filenames:
# files = ['python.png', 'qwerty.py', 'Python.PNg', 'apple.pnG', 'zebra.PNG', 'solution.Py', 'stepik.org', 
# 'kotlin.ko', 'github.git', 'ZeBrA.PnG']
# then the answer would be:
# apple.pngython.png zebra.png

files = [
    'python.png', 
    'qwerty.py', 
    'stepik.png', 
    'beegeek.org', 
    'windows.pnp', 
    'pen.txt', 
    'phone.py', 
    'book.txT', 
    'board.pNg', 
    'keyBoard.jpg', 
    'Python.PNg', 
    'apple.jpeg', 
    'png.png', 
    'input.tXt', 
    'split.pop', 
    'solution.Py', 
    'stepik.org', 
    'kotlin.ko', 
    'github.git'
    ]

print(*sorted(set(word.lower() for word in files if word[-4:].lower()==".png")))