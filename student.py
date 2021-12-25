import sys


class Student:

    def __init__(self, _name='John', _grade=1, _concentration='Foundations'):

        self.name = _name

        self.grade = _grade

        self.concentration = _concentration

        self.lowerDivCredit = 0

        self.upperDivCredit = 0

        self.lowerDiv = {
            210: ['Computer Science I', 0],
            211: ['Computer Science II', 0],
            212: ['Computer Science III', 0]
        }

        self.upperDiv = {
            313: ['Intermediate Data Structures', 0],
            314: ['Computer Organization', 0],
            315: ['Intermediate Algorithms', 0],
            330: ['C/C++ and Unix', 0],
            415: ['Operating Systems', 0],
            422: ['Software Methodology I', 0],
            425: ['Principles of Programming Languages', 0]
        }

        self.electives = {
            322: ['Introduction to Software Engineering', 0],
            333: ['Applied Cryptography', 0],
            372: ['Machine Learning for Data Science', 0],
            413: ['Advanced Data Structures', 0],
            420: ['Automata Theory', 0],
            423: ['Software Methodologies II', 0],
            427: ['Introduction to Logic', 0],
            429: ['Computer Architecture', 0],
            431: ['Introduction to Parallel Computing', 0],
            432: ['Intro to Computer Networks', 0],
            433: ['Computer & Network Security', 0],
            434: ['Computer and Network Security II', 0],
            436: ['Secure Software Development', 0],
            443: ['User Interfaces', 0],
            445: ['Modeling and Simulation', 0],
            451: ['Database Processing', 0],
            452: ['Database Issues', 0],
            453: ['Data Mining', 0],
            454: ['Bioinformatics', 0],
            455: ['Computational Science', 0],
            461: ['Introduction to Compilers', 0],
            471: ['Introduction to Artificial Intelligence', 0],
            472: ['Machine Learning', 0],
            473: ['Probabilistic Methods', 0],
            490: ['Computer Ethics', 0],
        }

        self.repeatable = {
            399: ['Various Lower Division Electives', 0],
            407: ['Various Seminars', 0],
            410: ['Various Upper Division Electives', 0]
        }

        self.requirementList = [False, False, False]


    def getValues(self, index):
        array = [self.lowerDiv, self.upperDiv, self.electives]
        array2 = [{}, {}, self.repeatable]
        arrayNames = ['Lower Division', 'Upper Division', 'Electives']
        return array[index], array2[index], arrayNames[index]

    def addClasses(self, index):
        array, array2, arrayNames = self.getValues(index)
        print('----------------------------------------------------------------------------------------------')
        print(f'\nAll possible {arrayNames} CIS courses:')
        print('_____________________________________________')

        for i in array:
            print(f'|{i}| {array[i][0]}')

        if array2:
            for i in array2:
                print(f'|{i}| {array2[i][0]}')

        print('_____________________________________________\n')
        print(f'Please enter all the  {arrayNames} CIS courses you have taken (i.e. Enter 415 for CIS 415).')
        print(f'Once you have finished entering classes, enter Done to progress.\n')

        while True:

            userInput = input('Course: ')

            if userInput == 'Done':
                confirmation = input('Are you sure? Enter y to confirm you have finished adding classes : ')
                if confirmation == 'y':
                    break

            try:
                courseNum = int(userInput)
                missingPrereqs = self.prereqs(courseNum, index)
                if missingPrereqs:
                    continue
                if courseNum in array and array[courseNum][1] == 0:
                    array[courseNum][1] += 1
                    print('Course added successfully')

                elif courseNum in array2:
                    array2[courseNum][1] += 1
                    print('Course added successfully')

                elif courseNum not in array:
                    print('This course does not exist!')

                else:
                    print('You have already added this course!')

            except ValueError:
                if userInput != 'Done':
                    print('Not a valid course number!')

    def DegreeProgressCore(self, index):
        array, array2, arrayNames = self.getValues(index)

        if all(value[1] == 1 for value in array.values()):
            self.requirementList[index] = True
            print(f'{arrayNames} courses completed')
            return

        if index != 1:
            print('You have not completed all the required Core courses yet.')
            self.missingClassRequirements(0)

            self.missingClassRequirements(1)

            sys.exit()

    def missingClassRequirements(self, index):
        array, array2, arrayNames = self.getValues(index)

        print(f'Your remaining required {arrayNames} classes are:')

        if self.requirementList[index]:
            return
        for i in array:
            if array[i][1] == 0:
                print(f'|{i}| {array[i][0]}')
        print('\n')

    def refactorClasses(self):
        for i in self.repeatable:

            if (self.repeatable[i][1] > 2) and (i != 410):
                print(
                    f'\nNote: Only 2 classes of CIS {i} will count towards degree requirements.\n'
                    f'You have enrolled in {self.repeatable[i][1]} courses of CIS {i}.\n'
                    f'The excess {self.repeatable[i][1] - 2} courses will not count toward degree requirements.\n')
                self.repeatable[i][1] = 2

    def degreeCompletion(self):
        setlist = set(self.requirementList)
        setLength = len(setlist)
        if setLength == 1 and setlist.pop() is True:
            print(f'\nCongratulations, {self.name}! You have successfully satisfied all CIS degree requirements!\n')
            return

        print(f'{self.name}, it appears you have not completed all degree requirements.\n')
        array = [0, self.missingClassRequirements, self.missingElectiveRequirements]

        for index, value in enumerate(self.requirementList):
            a, b, arrayNames = self.getValues(index)
            if not value:
                print(f'You have not completed the {arrayNames} requirements.')
                array[index](index)

    def missingElectiveRequirements(self, s):
        switchDictionary = self.switch()
        totalCreditSum = self.lowerDivCredit + self.upperDivCredit
        numClass = int(totalCreditSum / 4) if (totalCreditSum % 4) == 0 else totalCreditSum / 4

        # switchDictionary.popitem()
        untakenClasses = ['CIS ' + str(key) + ' ' + self.electives[key][0] for key in switchDictionary
                          if self.electives[key][1] != 1 and key in switchDictionary]

        classesLeft = 5 - numClass
        creditsLeft = 20 - totalCreditSum
        upperLeft = 3 - int(self.upperDivCredit / 4)

        requiredClass = switchDictionary[0]

        print(f'You currently have completed {totalCreditSum} elective credits '
              f'({self.upperDivCredit} upper division credits, {self.lowerDivCredit} lower division credits) '
              f'for a total of {numClass} classes. You need {creditsLeft} more elective credits (i.e. {classesLeft} '
              f'classes) to satisfy the 20 credit Requirement for electives.')

        if self.electives[requiredClass][1] == 0 and self.concentration != 'Foundations':
            print(f'You are missing the required class for your concentration - CIS {requiredClass} : '
                  f'{self.electives[requiredClass][0]} to satisfy the Primary Course Requirement.')

        if self.upperDivCredit < 12:
            bb = ', '.join(untakenClasses)
            print(f'Your current concentration, {self.concentration}, requires you to pick at least {upperLeft} '
                  f'more classes from {bb} to satisfy all upper division elective requirements.')

    def DegreeProgressElectives(self, electiveClasses):
        requiredClass = electiveClasses[0]

        for i in self.electives:
            if self.electives[i][1] == 1:
                if i in electiveClasses:
                    self.upperDivCredit += 4
                else:
                    self.lowerDivCredit += 4
                    if self.lowerDivCredit >= 8:
                        self.lowerDivCredit = 8
        if (self.upperDivCredit + self.lowerDivCredit) >= 20:
            if (self.concentration == 'Foundations') or (self.electives[requiredClass][1] == 1):
                self.requirementList[-1] = True

                print('All elective requirements have been completed.')
        print(f'Lower Division Electives Completed: {self.lowerDivCredit}')
        print(f'Upper Division Electives Completed: {self.upperDivCredit}')

    def repeatableElectives(self):
        for i in self.repeatable:
            if i == 410:
                if self.concentration == 'Foundations':
                    self.upperDivCredit += (4 * self.repeatable[410][1])
                else:
                    self.lowerDivCredit += (4 * self.repeatable[410][1])

            elif i == 399:
                self.lowerDivCredit += (4 * self.repeatable[399][1])
            elif i == 407:
                self.lowerDivCredit += (2 * self.repeatable[407][1])
            if self.lowerDivCredit >= 8:
                self.lowerDivCredit = 8

    def switch(self):
        switchStatement = {
            'Computational Science': [455, 443, 445, 451, 452, 453, 454, 471],
            'Computer Networks':     [432, 413, 429, 433, 445, 473],
            'Computer Security':     [433, 432, 472, 490],
            'Foundations':           [413, 420, 427, 429, 431, 432, 433, 434, 436,
                                      443, 445, 451, 452, 453, 454, 455, 461, 471,
                                      472, 473, 490],
            'Software Development':  [423, 413, 420, 427, 455, 461]
        }
        return switchStatement.get(self.concentration)

    def Concentration(self):
        switchDictionary = self.switch()
        self.repeatableElectives()
        self.DegreeProgressElectives(switchDictionary)

    def prereqs(self, course, index):
        array, array2, arrayNames = self.getValues(index)
        if index == 2:
            newarray, newarray2, newarrayNames = self.getValues(1)
        missingPrereqs = False


        prereq = {211: [210],
                  212: [211],
                  313: [212],
                  314: [212],
                  315: [313],
                  330: [314],
                  415: [313, 330],
                  425: [315],
                  413: [315],
                  420: [315],
                  422: [313],
                  423: [422],
                  431: [330],
                  432: [330],
                  433: [415],
                  434: [432, 433],
                  436: [330],
                  443: [313],
                  451: [313, 314],
                  461: [314, 425],
                  471: [315],
                  472: [315]
                  }

        try:
            prereq1 = prereq[course][0]
            prereq2 = prereq[course][-1]

            if index == 2 and course != 434:
                missingPrereqs = self.prereqClass(prereq1, prereq2, newarray, course, array)
            if missingPrereqs:
                return missingPrereqs

            if (array[prereq1][1] != 1 or array[prereq2][1] != 1) and course in array:
                missingPrereqs = self.prereqClass(prereq1, prereq2, array, course, array)

            return missingPrereqs

        except KeyError:
            return False

    def prereqClass(self, prereq1, prereq2, newarray, course, array):
        a = False
        if (newarray[prereq1][1] != 1 or newarray[prereq2][1] != 1) and course in array:
            print(f'{self.name}, you are missing the prerequisite courses:')
            if prereq1 != prereq2 and newarray[prereq2][1] != 1:
                print(f'CIS {prereq2} {newarray[prereq2][0]}')
            if newarray[prereq1][1] != 1:
                print(f'CIS {prereq1} {newarray[prereq1][0]}')
            a = True
        return a
