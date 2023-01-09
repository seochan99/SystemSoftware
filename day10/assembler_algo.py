def cal_object_code(loc_list, object_code, label, opcode, operand, instruction_code):
    # init
    for i in range(len(label)):
        # loc 계산
        # 시작부분인 START일때 '      '으로, 그외에는 0으로 초기화
        if opcode[i] == 'start':
            # start object_code is null
            object_code.append('         ')
            continue
        else:
            object_code.append('000000')

    for i in range(1, len(label)):
        flag1 = True
        flag2 = False
        # loc 계산
        # 시작부분인 START일때 '      '으로, 그외에는 0으로 초기화
        data = ''
        # instruction code가 있을때
        if opcode[i].upper() in instruction_code:
            # ldch, stch일 경우
            if opcode[i] == 'ldch' or opcode[i] == 'stch':
                # data붙이기
                data = data + instruction_code[f'{opcode[i].upper()}']
                # operand 쪼개주기 str1, x
                operand[i] = operand[i].split(',')
            else:
                data = data + instruction_code[f'{opcode[i].upper()}']
        # word가 들어올때
        elif opcode[i] == 'word':
            temp = int(operand[i])
            data = data + format(temp, 'x')

        # byte, char이 들어올때
        elif opcode[i] == 'byte':
            text = operand[i].split("\'")[1]
            # 아스키코드로 변환
            ascii_values = [ord(character) for character in text]
            for j in ascii_values:
                data = data + format(j, 'x')
        # 이때는 data값을 안가짐
        elif opcode[i] == 'resb' or opcode[i] == 'resw' or opcode[i] == 'end':
            data = '      '
        else:  # 잘못된 심볼
            flag1 = False

        # operand가 있는지 체크
        for j in range(1, len(label)):
            # 해당 operand 주소  붙이기
            # ldch, stch일때 str, x나눠져있음
            if opcode[i] == 'ldch' or opcode[i] == 'stch':
                # str이라고 변수 있다면
                if operand[i][0] in label[j]:
                    # 90붙이고 지시어 코드 붙이기
                    data = data + '90' + loc_list[j][2:4]
                    flag2 = True
            # 그외
            elif operand[i] in label[j]:
                if label[j] != 'first':
                    data = data + loc_list[j]
                flag2 = True
                break
            # word resb resw byte는 loc붙일거없음
            elif opcode[i] == 'word' or opcode[i] == 'resb' or opcode[i] == 'resw' or opcode[i] == 'byte':
                flag2 = True
                break

        # 해당 줄 출력하기
        # 심볼이 없을경우
        if flag1 == False:
            operand[i] = operand[i] + "\n**** unrecognized operation code ****"

        # operation code가 없을 경우
        if flag2 == False:
            operand[i] = operand[i] + "\n**** undefined symbol in operand ****"

        # 6자리가 안되면 0으로 채우기
        object_code[i] = data.zfill(6)
        # print(data.zfill(6))


def upperList(loc_list, object_code, label, opcode, operand):
    loc_list = [i.upper() for i in loc_list]
