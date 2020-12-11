import os
import re
import random

SPACES = 3
INDENT = SPACES * " "
ROOT_DIRECTORY = os.getcwd()
ID = random.randrange(1000, 9999)
FILE_NAME = "tree" + str(ID) + ".txt"
IGNORE = [ r'^\/?(?:\w+\/)*(\.\w+)', FILE_NAME ]
'''
    @returns: Boolean.
    @params: string item: file name.
    @desc: Returns True if file should be ignored based on its name.
'''
def _ignore(item):
    for pattern in IGNORE:
        if re.match(pattern, item): return True
'''
    @returns: Boolean.
    @params: string item, string directory
    @desc: Returns True if the item is a file name.
'''
def _isfile(item, directory):
    return (os.path.isfile(item) if directory == "." else os.path.isfile(os.path.join(directory, item)))
'''
    @returns: string.
    @params: string directory: key word arg defaults to "."
    @desc: Returns string representing current folders tree structure
'''
def _generate_tree(directory = "."):
    directory_items = os.listdir(directory)
    directory_path = ROOT_DIRECTORY if directory == "." else directory
    directory_path_array = directory_path.split("/")
    indents = len(directory.split("/"))
    
    Root = directory_path_array[-1]
    Tree = Root + "/" + "\n"

    for item in directory_items:
        if _ignore(item): continue
        
        Tree += indents * INDENT
        if _isfile(item, directory): 
            Tree += item + "\n"
        else: 
            Tree += _generate_tree(directory = directory + "/" + item)
                
    return Tree

def create_tree_file(filename = None):
    try:
        if filename is None: filename = FILE_NAME
        IGNORE.append(filename)
        file = open(filename, "w")
        tree = _generate_tree()
        file.write(tree)
        file.close()
        return True
    except Exception as e:
        file.close()
        print(e)


if __name__ == "__main__":
    create_tree_file()
