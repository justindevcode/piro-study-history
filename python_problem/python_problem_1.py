

num = 0
global lose
lose = None

def brGame(A , num):
    num2 = num
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
        print('player',A,' : ', num2)
        if num2 == 31:
            break
    if num2 == 31:
        return "B"
    else:
        return int(count)


while True:
    resolt = brGame('A', num)
    if resolt == 'B':
        print('playerB win!')
        break
    else:
        num +=resolt
    resolt = brGame('B', num)
    if resolt == 'A':
        print('playerA win!')
        num += resolt
        break
    else:
        num += resolt

