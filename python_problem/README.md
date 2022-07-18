파이썬 개인과제 1-8번수정 : 1-9번처럼 함수 리턴값 A로, 메인에서 if else문에 num += resolt두개있던거 수정
    if num2 == 31:
        return A
    else:
        return int(count)


while True:
    resolt = brGame('A', num)
    if resolt == 'A':
        print('playerB win!')
        break
    else:
        num +=resolt
    resolt = brGame('B', num)
    if resolt == 'B':
        print('playerA win!')
        break
    else:
        num += resolt