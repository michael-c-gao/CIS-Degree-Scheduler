

def addClasses(unrepeatable, repeatable, name):

    print('----------------------------------------------------------------------------------------------')
    print(f'\nAll possible {name} CIS courses:')
    print('_____________________________________________')

    for i in unrepeatable:
        print(f'|{i}| {unrepeatable[i][0]}')

    if repeatable:
        for i in repeatable:
            print(f'|{i}| {repeatable[i][0]}')

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


def DegreeProgressCore(classes, list, name, index):

    if all(value[1] == 1 for value in classes.values()):
        list[index] = True
        print(f'{name} courses completed')


def DegreeProgressElectives(classes, repeatableClasses, creditSum, list):

    lowerDivCredit = 0
    upperDivCredit = 0

    for j in repeatableClasses:
        if (repeatableClasses[j][1]) and (j == 410):
            upperDivCredit += 4*repeatableClasses[j][1]
        elif repeatableClasses[j][1]:
            if j == 399:
                lowerDivCredit += 4 * repeatableClasses[j][1]
            elif j == 407:
                lowerDivCredit += 2 * repeatableClasses[j][1]
            if lowerDivCredit >= 8:
                lowerDivCredit = 8


    for i in classes:
        courseLevel = (i // 100)
        if (classes[i][1]) and (courseLevel == 4):
            upperDivCredit += 4
        elif (classes[i][1]) and (courseLevel == 3):
            lowerDivCredit += 4
            if lowerDivCredit >= 8:
                lowerDivCredit = 8

    creditSum = creditSum + lowerDivCredit + upperDivCredit

    print(f'Lower Division Elective Credits:{lowerDivCredit}')
    print(f'Upper Division Elective Credits: {upperDivCredit}')
    print(f'Total Elective Credits Earned: {creditSum}')


    if ((upperDivCredit + lowerDivCredit) >= 20):
        list[2] = True
        print('All elective requirements satisfied.')



def refactorClasses(classes):

    for i in classes:

        if (classes[i][1] > 2) and (i == 399):
            print(
                f'\nNote: Only 2 classes of CIS {i} will count towards degree requirements for a total of 8 credits.\n'
                f'You have enrolled in {classes[i][1]} courses of CIS {i}.\n'
                f'The excess {classes[i][1] - 2} courses will not count toward degree requirements.\n')
            classes[i][1] = 2

        elif (classes[i][1] > 2) and (i == 407):
            print(
                f'\nNote: Only 2 classes of CIS {i} will count towards degree requirements for a total of 4 credits.\n'
                f'You have enrolled in {classes[i][1]} courses of CIS {i}.\n'
                f'The excess {classes[i][1] - 2} courses will not count toward degree requirements.\n')
            classes[i][1] = 2


def lowerDivisionRequirements(classes):

    for i in classes:
        if classes[i][1] == 0:
            print(f'|{i}| {classes[i][0]}')

def degreeCompletion(array):

    setlist = set(array)
    setLength = len(setlist)
    if setLength == 1 and setlist.pop() is True:
        print("\nCongratulations! You have successfully satisfied all CIS degree requirements!\n")


def prereqs():
    pass

def paths():
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
                   410 : ['Various Upper Division Electives', 0]
                   }

    prereq = { 315 : {313},
               330 : {314},
               415 : {313, 330},
               425: {315},
               413 : {315},
               420 : {315},
               422 : {313},
               423 : {422},
               431 : {330},
               432 : {330},
               433 : {415},
               434 : {432, 433},
               436 : {330},
               443 : {313},
               451 : {313,314},
               461 : {314, 425},
               471 : {315},
               472 : {315}
               }

    requirementList = [False, False, False]
    totalCreditSum = 0

    addClasses(lowerDiv, {}, 'lower division')

    DegreeProgressCore(lowerDiv, requirementList, 'Lower Division', 0)

    if requirementList[0]:
        addClasses(upperDiv, {}, 'upper division')

        DegreeProgressCore(upperDiv, requirementList, 'Upper Division', 1)

        addClasses(electives, repeatable, 'elective')
        refactorClasses(repeatable)

        DegreeProgressElectives(electives, repeatable, totalCreditSum, requirementList)

        degreeCompletion(requirementList)


    else:
        print("You have not completed all the required lower division courses yet.")
        print("Your remaining required Core classes are:")
        lowerDivisionRequirements(lowerDiv)
        lowerDivisionRequirements(upperDiv)


    print(lowerDiv)
    print(upperDiv)
    print(electives)
    print(repeatable)
    print(requirementList)


if __name__ == "__main__":
    main()
