
num=0
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
    print('playerA : ',num)