import random

num = 0
global lose
lose = None

def brGame(A , num):
    num2 = num
    if A == "computer":
        count = random.randint(1, 3)

    else:
        count = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")

        while (count != '1' and count != '2' and count != '3'):
            if not count.isdigit():
                print('정수를 입력하세요')
                count = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")
            else:
                print("1,2,3 중 하나를 입력하세요")
                count = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")

    for i in range(0, int(count)):
        num2 += 1
        print(A,' : ', num2)
        if num2 == 31:
            break
    if num2 == 31:
        return A
    else:
        return int(count)


while True:
    resolt = brGame('computer', num)
    if resolt == 'computer':
        print('player win!')
        break
    else:
        num +=resolt
    resolt = brGame('player', num)
    if resolt == 'player':
        print('computer win!')
        break
    else:
        num += resolt

