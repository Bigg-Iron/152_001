def get_grades():
    num_grades = int(input('How many grades:\n'))
    grades = []
    while len(grades) < num_grades:
        s = float(input('Enter grade: '))
        grades.append(s)
    return grades
    # pass


def average(grades):
    if grades[0] <= 0:
        avg = float(0)
        return avg
    else:
        total = 0
        for g in grades:
            total += g
            avg = float((total / len(grades)))
    return avg



def maximum(grades):
    maximum = 0
    if grades[0] <= 0:
        maximum = float(0)
        return maximum
    else:
        for grade in grades:
            if grade > maximum:
                maximum = grade
        return maximum


def minimum(grades):
    if grades[0] <= 0:
        minimum = float(0)
        return minimum
    else:
        minimum = grades[0]
        for grade in grades:
            if grade < minimum:
                minimum = float(grade)
        return minimum



def print_grades(grades):
    for grade in grades:
        print(grade)
    


def main():
    grades = get_grades()

    print_grades(grades)
    print("Average:", average(grades))
    print("Max:", maximum(grades))
    print("Min:", minimum(grades))


if __name__ == "__main__":
    main()
