from student import *

def initialInfo():

    a = {1, 2, 3, 4}
    b = {"Computational Science", "Computer Networks", "Computer Security", "Foundations", "Software Development", '1'}

    print("Welcome to the CIS Degree Scheduler! This program will show you which classes you need for your major, as "
          "well as plan out what you should take in the upcoming years.")
    name = input("Please enter your name: ")
    print(f'Welcome, {name}!')
    while True:
        year = input("Please enter your grade (1 for FR, 2 for SO, 3 for J, 4 for SR): ")
        try:
            yearNum = int(year)
            if yearNum in a:
                while True:
                    Concentration = input("Now please enter your concentration (Computational Science,"
                    " Computer Networks, Computer Security, Foundations, Software Development): ")
                    if Concentration in b:
                        break
                    print("This is not a valid concentration.")
                return name, yearNum, Concentration
            print("Not a valid year! Enter 1 for FR, 2 for SO, 3 for J, 4 for SR.")
        except ValueError:
                print("Please enter an integer! Enter 1 for FR, 2 for SO, 3 for J, 4 for SR.")



def main():


    LowerDiv = 0
    UpperDiv = 1
    Elective = 2

    name, grade, concentration = initialInfo()
    stud = Student(name, grade, concentration)

    stud.addClasses(LowerDiv)

    stud.DegreeProgressCore(LowerDiv)

    stud.addClasses(UpperDiv)
    stud.DegreeProgressCore(UpperDiv)

    stud.addClasses(Elective)
    stud.refactorClasses()
    stud.Concentration()


    stud.degreeCompletion()



if __name__ == "__main__":
    main()
