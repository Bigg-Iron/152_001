def writeToFile(string, filename):
    
    f = open('/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/activities/labs/L8/' + filename,"w") #opening file in write mode allows you to write something in the file
    f.write(string)
    pass

def printFile(filename):
    f = open('/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/activities/labs/L8/' + filename,"r")
    for line in f:
        print(line)
    pass

def writeListToFile(l, filename):
    f = open('/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/activities/labs/L8/' + filename,"w")
    
    for word in l:
        f.write(str(word))
    
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
    