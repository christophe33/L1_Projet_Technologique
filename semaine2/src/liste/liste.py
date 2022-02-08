class cell:

    def __init__(self, value = None, next = None):
        self.__value = value
        self.__next = next

    def setNext(self, next):
        self.__next = next

    def getNext(self):
        return self.__next

    def getValue(self):
        return self.__value

    def setValue(self, value):
        self.__value = value

            

class liste:

    def __init__(self):
        self.__head = None
        self.__last = None

    def isEmpty(self):
         return self.__head == None

    def addFirst(self, cell):
        if self.isEmpty():
            self.__head = cell
           
        else:
            ptr = self.__head
            self.__head = cell
            cell.setNext(ptr)
            self.__last = ptr

    def addLast(self, cell):
        if self.isEmpty():
            self.__head = cell
        else:
            self.__last.setNext(cell)
 

    def __str__(self):   
        resultat = ""
        ptr = self.__head   
        while ptr != None:  
            resultat = resultat + str(ptr.getValue()) + ' -> '
            ptr = ptr.getNext() 
        return resultat

    
    def getLast(self):
        return self.__last

    def getFirst(self):
        return self.__head
