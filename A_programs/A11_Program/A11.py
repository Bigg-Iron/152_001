# Your program should count the number of word occurrences contained in a file and 
# output a table showing the top 20 frequently used words in decreasing order of use.

def extract_words(string):
    """
    Returns a list containing each word in the string, ignoring punctuation, numbers, etc.
    DO NOT CHANGE THIS CODE
    """
    l = []
    word = ''
    for c in string+' ':
        if c.isalpha():
            word += c
        else:
            if word != '':
                l.append(word.lower())
            word = ''
    return l
  
def count_words(filename):
    """Returns a dictionary containing the number of occurrences of each word in the file."""
    # create a dictionary
    
    # open the file and read the text
    
    # extract each word in the file
    
    # count the number of times each word occurs.
    
    # return the dictionary with the word count.
    return 


def report_distribution(count):
    """Creates a string report of the top 20 word occurrences in the dictionary."""
    # create a list containing tuples of count and word,
    # while summing the total number of word occurrences
    
    # add lines with the title and total word count to the output string
    
    # sort the list from largest number to smallest,
    # add a line to the output for each word in the top 20 containing count and word
    
    # return the string containing the report
    return 


def main():
    """
    Prints a report with the word count for a file.
    DO NOT CHANGE THIS CODE
    """
    filename = input('filename?\n')
    print(report_distribution(count_words(filename)))


if __name__ == '__main__':
    main()
  