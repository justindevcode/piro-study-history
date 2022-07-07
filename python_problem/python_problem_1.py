
num=0
lose= None
while True:
    count = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")

    while (count != '1' and count != '2' and count != '3'):
        if not count.isdigit() :
            print('정수를 입력하세요')
            count = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")
        else :
            print("1,2,3 중 하나를 입력하세요")
            count = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")

    for i in range(0,int(count)):
        num += 1
        print('playerA : ', num)
        if num == 31:
            lose = "A";
            win = "B"
            break;

    if lose != None:
        break


    count = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")

    while (count != '1' and count != '2' and count != '3'):
        if not count.isdigit() :
            print('정수를 입력하세요')
            count = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")
        else :
            print("1,2,3 중 하나를 입력하세요")
            count = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")

    for i in range(0,int(count)):
        num += 1
        print('playerB : ', num)
        if num == 31:
            lose = "B";
            win = "A"
            break;
    if lose != None:
        break
print("player",win,"win!")