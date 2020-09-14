def average(grades): 
    total = 0
    e = 0
    while(e < len(grades)):
        total = total + grades[e]
        e += 1
    # print(total)
    average = total / len(grades)
    return(average)
    
    

def maximum(grades):
    maximum = grades[0]
    return(float(maximum))



def minimum(grades):
    minimum = min(grades)
    return(float(minimum))



def print_grades(grades):
    print(*grades, sep = "\n")


    


def get_grades():
    g = []
    while True:
        n = float(input("Enter grade:\n"))
        if n > 0:
            g.append(n)

        else:
            return g
            



   
        
 
    
    

    

def main():
    grades = get_grades()

    print_grades(grades)
    print("Average:", average(grades))
    print("Max:", maximum(grades))
    print("Min:", minimum(grades))

if __name__ == '__main__':
    main()
