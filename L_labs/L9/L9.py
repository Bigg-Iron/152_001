def processFile(filename):
    # Open file
    file = open('/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/activities/labs/L9/'+ filename, 'r')
    # Read line by line
    for line in file:
    # print the result of the call to processLine(line)
        print(processLine(line))
        
    pass


def processLine(line):
    # Split line by colon
    n = line.split(':')
    name = n[0].split(',')
    # call makeUsername with list item containing string of first and last name
    user_name = makeUserName(name)
    
    # call getAmount with list item containing the string holding amounts
    amounts = line.split(':')[-1]
    total_amounts = getAmount(amounts)
    
    # return the formatted string 'Username: name - Account Balance: 000000.00'
    # Username should be formatted with 7 characters right justified
    # Acount balance should formatted with 2 decimals left justified
    # return('Username: {name:>7} - Account Balance: {zero:<.2f}'.format(name,zero))
    # Hint use format string in dicsussed in 9.3. 
    # print('Username: {user_name:>7} {total_amounts:<.2f}'.format(user_name, total_amounts))
    return('Username: {:>7} - Account Balance: {:<.2f}'.format(user_name, total_amounts))
    # return(print('Username: {user_name:>7} - Account Balance: {total_amounts:<.2f}'.format(user_name, total_amounts)))
    pass

def makeUserName(user_name):
    # Split on comma
    # get first name from list
    first_name = user_name[0]
    # print('First name: {}, Last name: {}'.format(first_name))
    
    # get first character from first name
    # make the first char upper case
    F = first_name.upper()[0] 
    # get last name from list
    last_name = user_name[-1]
    # get characters 0->5 from last name
    # make those characters lowercase
    l = last_name.lower()[0:6]
    # return the two things above concatenated
    user_name = F + l
    return user_name
    pass

def getAmount(amounts):
    # split line on comma
    amounts_Split = amounts.split(',')
    # loop through amounts
    amounts = []
    for amount in amounts_Split:
        amounts.append(float(amount))
    # add the floating point values together
    total_amount = sum(amounts)
    # print(amounts)
    return total_amount
    pass

def main():
    filename = input("filename?\n")
    processFile(filename)
    
if __name__ == '__main__':
    main()