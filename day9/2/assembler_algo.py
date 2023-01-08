def cal_object_code(loc_list, object_code, label, opcode, operand, instruction_code):
    # init
    for i in range(len(label)):
        # loc 계산
        # 시작부분인 START일때 '      '으로, 그외에는 0으로 초기화
        if opcode[i] == 'start':
            # start object_code is null
            object_code.append('      ')
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
            data = data + instruction_code[f'{opcode[i].upper()}']
        # word가 들어올때
        elif opcode[i] == 'word':
            data = data + operand[i]
        # byte, char이 들어올때
        elif opcode[i] == 'byte':
            text = operand[i].split("\'")[1]
            # 아스키코드로 변환
            ascii_values = [ord(character) for character in text]
            for j in ascii_values:
                data = data + format(j, 'x')
        # 이때는 data값을 안가짐
        elif opcode[i] == 'resb' or 'resw' or 'end':
            data = '      '
        else:  # 잘못된 심볼
            flag1 = False

        # operand가 있는지 체크
        for j in range(1, len(label)):
            # 해당 operand 주소  붙이기
            if operand[i] == label[j]:
                data = data + loc_list[j]
                flag2 = True
                break

        # 해당 줄 출력하기
        # 심볼이 없을경우
        if flag1 == False:
            operand[i] = operand[i] + "\n**** undefined symbol in operand ****"

        # operation code가 없을 경우
        if flag2 == False:
            operand[i] = operand[i] + "\n**** unrecognized operation code ****"

        # 6자리가 안되면 0으로 채우기
        print(data.zfill(6))
