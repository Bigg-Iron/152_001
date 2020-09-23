def average(grades):
    total = 0
    grades = [0]
    e = 0
    if grades[0] <= 0:
        average = 0
        return(float(average))
    elif grades:
        while(e < len(grades)):
            total = total + grades[e]
            e += 1
            average = float(total / len(grades))
            return(float(average))
            
        


def maximum(grades):
    maximum = 0
    x = 0
    grades = [0]
    if len(grades) < 0:
        maximum = 0
        return maximum
    while (x < len(grades)):
        if len(grades) < 0:
            maximum = 0
            return maximum
        elif grades[x] > maximum:
            maximum = grades[x]
        else:
            x += 1
   
    return(float(maximum))



def minimum(grades):
    grades = [0]
    minimum = grades[0]
    z = 0
    while (z < len(grades)):
        if grades[z] < minimum:
            minimum = grades[z]
        else:
            z += 1

    return(float(minimum))


def print_grades(grades):
    print(*grades, sep="\n")


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
