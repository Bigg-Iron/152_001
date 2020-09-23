def writeToFile(string, filename):
    pass

def printFile(filename):
    pass

def writeListToFile(l, filename):
    pass
    
def writeUserInfo(name, password, filename):
    pass
    
def sumFile(filename):
    pass
    
def nameInFile(user, filename):
    pass

def main():
    writeToFile("Hello, World\n", "hello.txt")
    printFile("hello.txt") 
    writeListToFile([1,2,3,4], "myfile.txt")
    printFile("myfile.txt") 
    writeUserInfo("casey","walrus7","secret_file")
    writeUserInfo("riley","python_is_fun","secret_file")
    printFile("secret_file")
    print(sumFile("myfile.txt"))
    print(nameInFile('casey', 'secret_file'))
    
if __name__ == '__main__':
    main()
    