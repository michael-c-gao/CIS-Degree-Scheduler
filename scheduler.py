

def addClasses(unrepeatable, repeatable, name):
    print('----------------------------------------------------------------------------------------------')
    print(f'\nAll possible {name} CIS courses:')
    print('_____________________________________________')

    for i in unrepeatable:
        print(f'|{i}| {unrepeatable[i][0]}')

    print('_____________________________________________\n')
    print(f'Please enter all the  {name} CIS courses you have taken (i.e. Enter 415 for CIS 415).')
    print(f'Once you have finished entering classes, enter Done to progress.\n')

    while True:

        userInput = input("Course: ")

        if userInput == 'Done':
            confirmation = input("Are you sure? Enter 'y' to confirm you have finished adding classes : ")
            if confirmation == 'y':
                break

        try:
            courseNum = int(userInput)
            if courseNum in unrepeatable and unrepeatable[courseNum][1] == 0:
                unrepeatable[courseNum][1] += 1

            elif courseNum in repeatable:
                repeatable[courseNum][1] += 1


            elif (courseNum not in unrepeatable):
                print('This course does not exist!')

            else:
                print('You have already added this course!')


        except ValueError:
            if userInput != 'Done':
                print("Not a valid course number!")


def DegreeProgress(classes, list, name):
    if all(value1[1] == 1 for value1 in classes.values()):
        list[0] = True
        print(f'{name} courses completed')


def prereqs():
    pass


def main():


    lowerDiv = { 210 : ['Computer Science I', 0],
                 211 : ['Computer Science II', 0],
                 212 : ['Computer Science III', 0]
                 }

    upperDiv = { 313 : ['Intermediate Data Structures', 0],
                 314 : ['Computer Organization', 0],
                 315 : ['Intermediate Algorithms', 0],
                 330 : ['C/C++ and Unix', 0],
                 415 : ['Operating Systems', 0],
                 422 : ['Software Methodology I', 0],
                 425 : ['Principles of Programming Languages', 0]
                 }

    electives = { 322 : ['Introduction to Software Engineering', 0],
                  333 : ['Applied Cryptography', 0],
                  372 : ['Machine Learning for Data Science', 0],
                  413 : ['Advanced Data Structures', 0],
                  420 : ['Automata Theory', 0], 423 : ['Software Methodologies II', 0],
                  431 : ['Introduction to Parallel Computing', 0],
                  432 : ['Intro to Computer Networks', 0],
                  433 : ['Computer & Network Security', 0],
                  434 : ['Computer and Network Security II', 0],
                  436 : ['Secure Software Development', 0],
                  443 : ['User Interfaces', 0],
                  451 : ['Database Processing', 0],
                  461 : ['Introduction to Compilers', 0],
                  471 : ['Introduction to Artificial Intelligence', 0],
                  472 : ['Machine Learning', 0]
                  }

    repeatable = { 399 : ['Various Lower Division Electives', 0],
                   407 : ['Various Seminars', 0],
                   410 : ['Various Lower Division Electives', 0] }

    requirementList = [False, False, False]

    addClasses(lowerDiv, {}, 'lower division')

    addClasses(upperDiv, {}, 'upper division')

    addClasses(electives, repeatable, 'elective')

    DegreeProgress(lowerDiv, requirementList, 'Lower Division')
    DegreeProgress(upperDiv, requirementList,  'Upper Division')


    print(lowerDiv)
    print(upperDiv)
    print(electives)
    print(repeatable)
    print(DegreeProgress)

if __name__ == "__main__":
    main()
