def processFile(filename):
    # Open file
    # Read line by line
    # print the result of the call to processLine(line)
    pass


def processLine(line):
    # Split line by colon
    # call makeUsername with list item containing string of first and last name
    # call getAmount with list item containing the string holding amounts
    # return the formatted string 'Username: name - Account Balance: 000000.00'
    # Username should be formatted with 7 characters right justified
    # Acount balance should formatted with 2 decimals left justified
    # Hint use format string in dicsussed in 9.3. 
    pass

def makeUserName(user_name):
    # Split on comma
    # get first name from list
    # get first character from first name
    # make the first char upper case
    
    # get last name from list
    # get characters 0->5 from last name
    # make those characters lowercase
    # return the two things above concatenated
    pass

def getAmount(amounts):
    # split line on comma
    # loop through amounts
    # add the floating point values together
    pass

def main():
    filename = input("filename?\n")
    processFile(filename)
    
if __name__ == '__main__':
    main()