import os
import re
import random

class TreeGenerator:
    def __init__(self):
        '''
        @defaults:
            1. Ignore dot files
            2. Default indents is 3 spaces
            3. Root directory is the current directory
        '''
        self.IGNORE = [ r'^\/?(?:\w+\/)*(\.\w+)' ]
        self.SPACES = 3
        self.INDENT = self.SPACES * " "
        self.ROOT_DIRECTORY = os.getcwd()
        self.ID = random.randrange(1000, 9999)
        self.FILE_NAME = "tree" + str(self.ID) + ".txt"
    '''
        @returns: Boolean.
        @params: string item: file name.
        @desc: Returns True if file should be ignored based on its name.
    '''
    def _ignore_(self, item):
        for pattern in self.IGNORE:
            if re.match(pattern, item): return True
    '''
        @returns: Boolean.
        @params: string item, string directory
        @desc: Returns True if the item is a file name.
    '''
    def _isfile_(self, item, directory):
        return (os.path.isfile(item) if directory == "." else os.path.isfile(os.path.join(directory, item)))
    '''
        @returns: string.
        @params: string directory: key word arg defaults to "."
        @desc: Returns string representing current folders tree structure
    '''
    def _generate_tree_(self, directory = "."):
        directory_items = os.listdir(directory)
        directory_path = self.ROOT_DIRECTORY if directory == "." else directory
        directory_path_array = directory_path.split("/")
        indents = len(directory.split("/"))
        
        Root = directory_path_array[-1]
        Tree = Root + "/" + "\n"

        for item in directory_items:
            if self._ignore_(item): continue
            
            Tree += indents * self.INDENT
            if self._isfile_(item, directory): 
                Tree += item + "\n"
            else: 
                Tree += self._generate_tree_(directory = directory + "/" + item)
                    
        return Tree

    def create_tree_file(self, filename = None):
        try:
            if filename is None: filename = self.FILE_NAME
            self.IGNORE.append(filename)
            file = open(filename, "w")
            tree = self._generate_tree_()
            file.write(tree)
            file.close()
            return True
        except Exception as e:
            file.close()
            print(e)


if __name__ == "__main__":
    MyTree = TreeGenerator()
    MyTree.create_tree_file()
