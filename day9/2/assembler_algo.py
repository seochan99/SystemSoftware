def cal_object_code(loc_list, object_code, label, opcode, operand):
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
        # loc 계산
        # 시작부분인 START일때 '      '으로, 그외에는 0으로 초기화
        if opcode[i] == 'start':
            # start object_code is null
            object_code.append('      ')
            continue
        else:
            object_code.append('000000')
