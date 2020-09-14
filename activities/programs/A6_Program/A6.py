def average(grades): 
    total = 0
    e = 0
    while(e < len(grades)):
        total = total + grades[e]
        e += 1
    average = float(total / len(grades))
    return(float(average))
    
    

def maximum(grades):
    maximum = grades[0]
    x = 0
    while (x < len(grades)):
        if grades[x] > maximum:
            maximum = grades[x]
        else:
            x += 1
            
    return(float(maximum))



def minimum(grades):
    minimum = grades[0]
    z = 0
    while (z < len(grades)):
        if grades[z] < minimum:
            minimum = grades[z]
        else:
            z += 1
            
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
