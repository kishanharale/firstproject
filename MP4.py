#
# Machine Problem 4
#
# Name      : Kishan rao Harale
# Banner Id : 001317675
#
# Python script that reads data in from the text file ‘5930 – MP4 Data.txt’. The
# file contains information about students in a class who have taken 3 exams.
#  This program will...
# (1) Print the student’s information out in the original form
# (2) Sort the data by the student’s last name
# (3) Print the information, again
# (4) Sort the data by the student’s test average
# (5) Print the information 1 more time.


def getScores():
    #
    # Opens the data file of names and scores... firstName, lastName, score1,
    # score2, score3... reads each line of data as a str, divides the line into
    # the 5 values... str, str, int, int, int... puts those values in a list,
    # and returns a list of those lists.
    #
    # There are no parameters.
    #
    # Returns a list of lists... each list contains a str, str, int, int, int.
    # < the body of your function getScores() goes here >

    student = []
    with open(
        "C:\\Users\\pallavi\\Desktop\\PYTHON CODINGS\\5930 - MP4 Data.txt"
    ) as score:
        student = score.readlines()
        student_list = []
        for line in student:
            student = line.split(" ")
            student[2] = int(student[2])
            student[3] = int(student[3])
            temp = student[4].split("\n")
            student[4] = int(temp[0])
            student_list.append(student)

        return student_list


def addTestAverage(studentScores):
    #
    # Finds the average of each student's test scores, and then appends that
    # average onto the end of that student's list. So, each student list now
    # contains str, str, int, int, int, float.
    #
    # studentScores A list of lists, each list contains a str, str, int,
    # int, int which are firstName, lastName, test1, test2,
    # test3.
    #
    # There is no return value.
    #
    # < the body of your function addTestAverage() goes here >
    student_score = []
    for i in range(len(studentScores)):
        student_score = studentScores[i]
        avg = (student_score[2] + student_score[3] + student_score[4]) / 3
        student_score.append(avg)


def calcTotals(studentScores):
    #
    # Finds the average of test1, test2, test3, and the total average. Returns
    # those 4 values in a list.
    #
    # studentScores A list of lists, each list contains a str, str, int,
    # int, int, float which are firstName, lastName, test1,
    # test2, test3, average.
    #
    # Returns a list with 4 values... float, float, float, float... which are
    # test1 avg, test2 avg, test3 avg, total avg.
    #
    # < the body of your function calcTotals() goes here >
    
    totals = []
    stuudent_exam = []

    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    for i in range(len(studentScores)):
        stuudent_exam = studentScores[i]
        sum1 += stuudent_exam[2]
        sum2 += stuudent_exam[3]
        sum3 += stuudent_exam[4]
        sum4 += stuudent_exam[5]
    totals = [
        sum1 / len(studentScores),
        sum2 / len(studentScores),
        sum3 / len(studentScores),
        sum4 / len(studentScores),
    ]
    return totals


def printScores(studentScores, totals):
    #
    # Prints out the entire list including firstName, lastName, score1, score2,
    # score3, average. There is a header for each column. The totals are
    # printed at the end.
    #
    # studentScores A list of lists, each list contains a str, str, int,
    # int, int, float which are firstName, lastName, test1,
    # test2, test3, average.
    # totals A list of 4 float values... the averages for test1,
    # test2, test3, and totalAverage.
    #
    # There is no return value.
    #
    # < the body of your function printScores() goes here >

    print(f"{'Name':<23}{'Exam1':>8}{'Exam2':>8}{'Exam3':>8}{'Avg':>8}")
    for a, b, c, d, e, f in studentScores:
        print(f"{a+' '+b:<23}{c:>8}{d:>8}{e:>8}{f:>8.2f}")
    print(
        f"{'Total':<23}{totals[0]:>8.2f}{totals[1]:>8.2f}{totals[2]:>8.2f}{totals[3]:>8.2f}"
    )


def sortByName(studentScores):
    #
    # Sorts the list of student info by the student's last name. Uses the
    # Bubble Sort algorithm.
    #
    # studentScores A list of lists, each list contains a str, str, int,
    # int, int, float which are firstName, lastName, test1,
    # test2, test3, average.
    #
    # There is no return value.
    #
    # < the body of your function sortByName() goes here >

    for i in range(len(studentScores) - 1):
        for j in range(len(studentScores) - 1):
            if studentScores[j][1] > studentScores[j + 1][1]:
                temp = studentScores[j]
                studentScores[j] = studentScores[j + 1]
                studentScores[j + 1] = temp


def sortByAverage(studentScores):
    #
    # Sorts the list of student info by the test average. Uses the
    # Bubble Sort algorithm.
    #
    # studentScores A list of lists, each list contains a str, str, int,
    # int, int, float which are firstName, lastName, test1,
    # test2, test3, average.
    #
    # There is no return value.
    #
    # < the body of your function sortByAverage() goes here >

    for i in range(len(studentScores) - 1):
        for j in range(len(studentScores) - 1):
            if studentScores[j][5] < studentScores[j + 1][5]:
                temp = studentScores[j]
                studentScores[j] = studentScores[j + 1]
                studentScores[j + 1] = temp


studentScores = getScores()
addTestAverage(studentScores)
totals = calcTotals(studentScores)
printScores(studentScores, totals)
print()
sortByName(studentScores)
printScores(studentScores, totals)
print()
sortByAverage(studentScores)
printScores(studentScores, totals)
