def addClasses(unrepeatable, repeatable):

    print("Please enter all CIS courses you have taken (i.e. Enter 415 for CIS 415).")
    # print("The CIS courses offered at the University of Oregon are:" )

    while True:

        userInput = input("Course: ")

        # print(userInput)
        if userInput == 'Done':
            confirmation = input("Are you sure? Enter 'y' to confirm you have finished adding classes : ")
            if confirmation == 'y':
                break

        try:
            courseNum = int(userInput)
            if courseNum in unrepeatable and unrepeatable[courseNum] == 0:
                unrepeatable[courseNum] += 1

            elif courseNum in repeatable:
                repeatable[courseNum] += 1


            elif (courseNum not in unrepeatable):
                print('This course does not exist!')

            else:
                print('You have already added this course!')


        except ValueError:
            if userInput != 'Done':
                print("Not a valid course number!")

def prereqs():
    pass

def DegreeProgress():
    pass


def main():

    unrepeatable = {210: 0, 211: 0, 212: 0, 313: 0, 314: 0, 315: 0, 322: 0,
                    330: 0, 333: 0, 372: 0, 415: 0, 425: 0, 413: 0, 420: 0,
                    422: 0, 423: 0, 431: 0, 432: 0, 433: 0, 434: 0, 436: 0,
                    443: 0, 451: 0, 461: 0, 471: 0, 472: 0}

    repeatable = {399: 0, 407: 0, 410: 0}

    addClasses(unrepeatable, repeatable)
    print(repeatable)
    print(unrepeatable)


if __name__ == "__main__":
    main()
