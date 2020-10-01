def readLettersFromFile(filename):
    """ Return all characters from file in a list"""
    return []

def countLetters(lettersFromFile):
    """Return dictionary of key:value pairs (letter,# times letter appears in file)"""
    return {}
    
def sortByCount(count):
    """Return list of tuples (value,key), sorted by value"""
    return []
        
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