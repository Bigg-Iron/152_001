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
        f.write('\n')
    
    pass
    
def writeUserInfo(name, password, filename):
    f = open('/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/activities/labs/L8/' + filename,"a")
    
    f.write('name=')
    f.write(name)
    f.write('\n')
    f.write('password=')
    f.write(password)
    f.write('\n')
    pass

# FIXME: sumFile(filename)
def sumFile(filename):
    f = open('/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/activities/labs/L8/' + filename,"w+")
    s = [float()]
    
    for line in f:
        s.append(line[:-1])
    print(s)
    pass
    
    
def nameInFile(user, filename):
    f = open('/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/activities/labs/L8/' + filename,"r")
    
    for line in f:
        if user in line:
            return True
        else:
            return False
    
    pass

def main():
    writeToFile("Hello, World\n", "hello.txt")
    printFile("hello.txt") 
    writeListToFile([1,2,3,10], "myfile.txt")
    printFile("myfile.txt") 
    writeUserInfo("casey","walrus7","secret_file")
    writeUserInfo("riley","python_is_fun","secret_file")
    printFile("secret_file")
    print(sumFile("test.txt"))
    print(nameInFile('casey', 'secret_file'))
    
if __name__ == '__main__':
    main()
    