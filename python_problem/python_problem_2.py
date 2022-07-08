#함수 이름은 변경 가능합니다.
# array = [[0 for col in range(4)] for row in range(1)]
# for i in array:
#     for j in i:
#         print(j ,end=" ")
#     print()
class AlreadyStudent(Exception):
    def __init__(self):
        super().__init__('already existing student!')

class NegatinbeInteger(Exception):
    def __init__(self):
        super().__init__('Negative integers are not allowed!')

class Notexistname(Exception):
    def __init__(self):
        super().__init__('Not exist name!')
class NoGradingdata(Exception):
    def __init__(self):
        super().__init__('No Grading data!')

class Nostudentdata(Exception):
    def __init__(self):
        super().__init__('No student data!')

array = []
##############  menu 1
def Menu1(name, mscore, fscore) :
    array.append([name, mscore, fscore,0])

##############  menu 2
def Menu2() :
    for i in range(len(array)):
        if (int(array[i][1]) + int(array[i][2]))/2 >= 90:
            array[i][3] = 'A'
        elif (int(array[i][1]) + int(array[i][2]))/2 >= 80:
            array[i][3] = 'B'
        elif (int(array[i][1]) + int(array[i][2]))/2 >= 70:
            array[i][3] = 'C'
        else:
            array[i][3] = 'D'



##############  menu 3
def Menu3() :
    print("-----------------------------------")
    print("name    mid    final    grade")
    print("-----------------------------------")

    for i in range(len(array)):
        if array[i][3] != 0:
            for j in range(4):
                print(array[i][j], end="       ")
            print()
    # for i in range(len(array)-1):
    #     if array[i][3] != 0:
    #         for j in i:
    #             if j == 0:
    #                 print('%-10s' % (j), end=' ')
    #             else:
    #                 print(j,end='   ')
    #         print()

##############  menu 4
def Menu4(name):
    name = name
    for i in range(len(array)):
        if array[i][0] == name:
            del array[i]
            break
    print(name,' student information is deleted.')

#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        try:
            delarray = []
            name, mscore, fscore = input('Enter name mid-score final-score : ').split()
            if int(mscore) < 0 or int(fscore) < 0:
                raise NegatinbeInteger

            for i in range(len(array)):
                if array[i][0] == name:
                    delarray.append(1)

            if len(delarray) == 1:
                raise AlreadyStudent
            Menu1(name, mscore, fscore)
        except NegatinbeInteger as e:
            print(e)
        except AlreadyStudent as e:
            print(e)
        except:
            print('Num of data id not 3!')


    elif choice == "2" :
        try:
            if len(array) == 0:
                raise Nostudentdata
            Menu2()
            print("Grading to all students.")
        except Nostudentdata as e:
            print(e)
        # if len(array) == 0:
        #     print("No student data!")
        # else:
        #     Menu2()
        #     print("Grading to all students.")
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우 2번 함수 호출
        #"Grading to all students." 출력

    elif choice == "3" :
        count = 0
        for i in range(len(array)):
            if array[i][3] == 0:
                count += 1
        try:
            if len(array) == 0:
                raise Nostudentdata
            elif count == len(array):
                raise NoGradingdata
            Menu3()
        except Nostudentdata as e:
            print(e)
        except NoGradingdata as e:
            print(e)
        # if len(array) == 0:
        #     print("No student data!")
        # elif count == len(array):
        #     print("No Grading data!")
        # else:
        #     Menu3()



        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        #예외사항이 아닌 경우 3번 함수 호출

    elif choice == "4" :
        try:
            name = input("Enter the name to delete : ")
            delarray = []

            for i in range(len(array)):
                if array[i][0] == name:
                    delarray.append(1)

            if len(delarray) == 0:
                raise Notexistname
            Menu4(name)
        except Notexistname as e:
            print(e)

        # name = input("Enter the name to delete : ")
        # Menu4(name)
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력

    elif choice == "5" :
        print("Exit Program!")
        break
        #프로그램 종료 메세지 출력
        #반복문 종료

    else :
        print("Wrong number. Choose again.")
        #"Wrong number. Choose again." 출력