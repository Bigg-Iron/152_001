def readLettersFromFile(filename):
    """ Return all characters from file in a list"""
    with open(filename, 'r+') as f:
        x = f.readlines()
        li = []
        for line in x:
            line.strip()
            for char in line:
                char.strip('\n')
                if char != ' ' and char != '\n':
                    li.append(char)
                else:
                   continue 
    return li

def countLetters(lettersFromFile):
    """Return dictionary of key:value pairs (letter,# times letter appears in file)"""
    l = lettersFromFile
    tally = dict((x,l.count(x)) for x in sorted(set(l)))
    return tally
    
def sortByCount(count):
    """Return list of tuples (value,key), sorted by value"""
    new_tuple = list(count.items())
    reversed_Tuple = [(v, k) for k, v in new_tuple]
    TTT = sorted(reversed_Tuple, key=lambda x: x)
    return TTT 
        
def main():
    """DO NOT CHANGE THIS"""
    filename = input("filename?\n")
    letters = readLettersFromFile(filename)
    print("Letters:", letters)
    
    count = countLetters(letters)
    print("Counted Letters", count)
    
    countSorted = sortByCount(count)
    print("Sorted:", countSorted)

if __name__ == "__main__":
    main()
    