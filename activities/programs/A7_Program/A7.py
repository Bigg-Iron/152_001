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
        avg = 0
        return avg
    
    else:
        total = 0
        for g in grades:
            total += g
            avg = (total / len(grades))
    return avg
    
    # pass


def maximum(grades):
    pass


def minimum(grades):
    pass


def print_grades(grades):
    for grade in grades:
        print(grade)
    
    # pass


def main():
    grades = get_grades()

    print_grades(grades)
    print("Average:", average(grades))
    print("Max:", maximum(grades))
    print("Min:", minimum(grades))


if __name__ == "__main__":
    main()
