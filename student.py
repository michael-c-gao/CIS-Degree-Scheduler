import sys

class Student:


    def __init__(self, _name='John', _grade=1, _concentration='Foundations'):

        self.name = _name

        self.grade = _grade

        self.concentration = _concentration

        self.lowerDivCredit = 0

        self.upperDivCredit = 0

        self.totalCreditSum = 0

        self.requirementList = [False, False, False]

        self.lowerDiv = {
            210 : ['Computer Science I', 0],
            211 : ['Computer Science II', 0],
            212 : ['Computer Science III', 0]
        }

        self.upperDiv = {
            313 : ['Intermediate Data Structures', 0],
            314 : ['Computer Organization', 0],
            315 : ['Intermediate Algorithms', 0],
            330 : ['C/C++ and Unix', 0],
            415 : ['Operating Systems', 0],
            422 : ['Software Methodology I', 0],
            425 : ['Principles of Programming Languages', 0]
        }

        self.electives = {
            322 : ['Introduction to Software Engineering', 0],
            333 : ['Applied Cryptography', 0],
            372 : ['Machine Learning for Data Science', 0],
            413 : ['Advanced Data Structures', 0],
            420 : ['Automata Theory', 0], 423 : ['Software Methodologies II', 0],
            427 : ['Introduction to Logic', 0],
            429 : ['Computer Architecture', 0],
            431 : ['Introduction to Parallel Computing', 0],
            432 : ['Intro to Computer Networks', 0],
            433 : ['Computer & Network Security', 0],
            434 : ['Computer and Network Security II', 0],
            436 : ['Secure Software Development', 0],
            443 : ['User Interfaces', 0],
            445 : ['Modeling and Simulation',0],
            451 : ['Database Processing', 0],
            452 : ['Database Issues', 0],
            453 : ['Data Mining', 0],
            454 : ['Bioinformatics', 0],
            455 : ['Computational Science', 0],
            461 : ['Introduction to Compilers', 0],
            471 : ['Introduction to Artificial Intelligence', 0],
            472 : ['Machine Learning', 0],
            473 : ['Probabilistic Methods', 0],
            490 : ['Computer Ethics', 0],
        }

        self.repeatable = {
            399: ['Various Lower Division Electives', 0],
            407: ['Various Seminars', 0],
            410: ['Various Upper Division Electives', 0]
        }

        self.array = [self.lowerDiv, self.upperDiv, self.electives]

        self.arrayNames = ['Lower Division', 'Upper Division', 'Electives']

        self.array2 = [{}, {}, self.repeatable]


    def addClasses(self, index):

        print('----------------------------------------------------------------------------------------------')
        print(f'\nAll possible {self.arrayNames[index]} CIS courses:')
        print('_____________________________________________')

        for i in self.array[index]:
            print(f'|{i}| {self.array[index][i][0]}')

        if self.array2[index]:
            for i in self.array2[index]:
                print(f'|{i}| {self.array2[index][i][0]}')

        print('_____________________________________________\n')
        print(f'Please enter all the  {self.arrayNames[index]} CIS courses you have taken (i.e. Enter 415 for CIS 415).')
        print(f'Once you have finished entering classes, enter Done to progress.\n')

        while True:

            userInput = input("Course: ")

            if userInput == 'Done':
                confirmation = input("Are you sure? Enter 'y' to confirm you have finished adding classes : ")
                if confirmation == 'y':
                    break

            try:
                courseNum = int(userInput)
                print(courseNum)
                if courseNum in self.array[index] and self.array[index][courseNum][1] == 0:
                    self.array[index][courseNum][1] += 1

                elif courseNum in self.array2[index]:
                    self.array2[index][courseNum][1] += 1


                elif courseNum not in self.array[index]:
                    print('This course does not exist!')

                else:
                    print('You have already added this course!')

            except ValueError:
                if userInput != 'Done':
                    print("Not a valid course number!")


    def DegreeProgressCore(self, index):

        if all(value[1] == 1 for value in self.array[index].values()):
            self.requirementList[index] = True
            print(f'{self.arrayNames[index]} courses completed')
            return

        if index != 1:
            print(f'You have not completed all the required {self.arrayNames[index]} courses yet.')
            print("Your remaining required Core classes are:")

            self.missingClassRequirements(0)
            self.missingClassRequirements(1)


            sys.exit()


    def missingClassRequirements(self, index):

        if self.requirementList[index]:
            return
        for i in self.array[index]:
            if self.array[index][i][1] == 0:
                print(f'|{i}| {self.array[index][i][0]}')


    def refactorClasses(self):

        for i in self.repeatable:

            if (self.repeatable[i][1] > 2) and (i != 410):
                print(
                    f'\nNote: Only 2 classes of CIS {i} will count towards degree requirements.\n'
                    f'You have enrolled in {self.repeatable[i][1]} courses of CIS {i}.\n'
                    f'The excess {self.repeatable[i][1] - 2} courses will not count toward degree requirements.\n')
                self.repeatable[i][1] = 2
        print(self.repeatable)


    def DegreeProgressElectives(self):

        if (self.repeatable[410][1]):
            self.upperDivCredit += 4 * self.repeatable[410][1]
        elif self.repeatable[399][1]:
            self.lowerDivCredit += 4 * self.repeatable[399][1]
        elif self.repeatable[407][1]:
            self.lowerDivCredit += 2 * self.repeatable[407][1]
        if self.lowerDivCredit >= 8:
            self.lowerDivCredit = 8

        for i in self.electives:
            courseLevel = (i // 100)
            if (self.electives[i][1]) and (courseLevel == 4):
                self.upperDivCredit += 4
            elif (self.electives[i][1]) and (courseLevel == 3):
                self.lowerDivCredit += 4

                if self.lowerDivCredit >= 8:
                    self.lowerDivCredit = 8

        self.totalCreditSum += (self.lowerDivCredit + self.upperDivCredit)

        print(f'Lower Division Elective Credits Earned:{self.lowerDivCredit}')
        print(f'Upper Division Elective Credits Earned: {self.upperDivCredit}')
        print(f'Total Elective Credits Earned: {self.totalCreditSum}')

        if (self.lowerDivCredit + self.upperDivCredit) >= 20:
            self.requirementList[-1]  = True
            print('All elective requirements satisfied.')


    def degreeCompletion(self):

        setlist = set(self.requirementList)
        setLength = len(setlist)
        if setLength == 1 and setlist.pop() is True:
            print("\nCongratulations! You have successfully satisfied all CIS degree requirements!\n")




