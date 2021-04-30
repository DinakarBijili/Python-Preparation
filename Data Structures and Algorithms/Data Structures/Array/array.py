class Array(object):
    def __init__(self, sizeOfArray, arrayType = int):
        self.sizeOfArray = len(list(map(arrayType, range(sizeOfArray))))
        self.arrayItems =[arrayType(0)] * sizeOfArray    # initialize array with zeroes
        
    def __str__(self):
            return ' '.join([str(i) for i in self.arrayItems])
            
    # function for search
    def search(self, keyToSearch):
        for i in range(self.sizeOfArray):
            if (self.arrayItems[i] == keyToSearch):    # brute-forcing
                return i     # index at which element/ key was found
            
        return -1          # if key not found, return -1
    
    # function for inserting an element
    def insert(self, keyToInsert, position):
        if(self.sizeOfArray > position):
            for i in range(self.sizeOfArray - 2, position - 1, -1):
                self.arrayItems[i + 1] = self.arrayItems[i]
            self.arrayItems[position] = keyToInsert
        else:
            print('Array size is:', self.sizeOfArray)
            
    # function to delete an element
    def delete(self, keyToDelete, position):
        if(self.sizeOfArray > position):
            for i in range(position, self.sizeOfArray - 1):
                self.arrayItems[i] = self.arrayItems[i + 1]
        else:
            print('Array size is:', self.sizeOfArray)
"""
1. Search 
2. insert 
3. Delete
"""

a = Array(10, int)
#Search
index = a.search(0)
# print(index)

#Insert
a.insert(1,2)
a.insert(2,3)
a.insert(3,4)
print(a)

#Delete
a.delete(3,4)
print(a)

#OUTPUT:-
# 0 0 1 2 3 0 0 0 0 0
# 0 0 1 2 0 0 0 0 0 0