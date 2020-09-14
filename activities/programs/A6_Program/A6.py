def average(grades):
    pass

def maximum(grades):
    pass

def minimum(grades):
    pass

def print_grades(grades):
    pass

def get_grades():
    a = []
    
    while True:
        n = float(input("Enter grade:\n"))
        if n > 0:
            a.append(n)
        else:
            # print(a)
            print(*a, sep = "\n") 
            break

   
        
 
    
        


    

def main():
    grades = get_grades()

    print_grades(grades)
    print("Average:", average(grades))
    print("Max:", maximum(grades))
    print("Min:", minimum(grades))

if __name__ == '__main__':
    main()
