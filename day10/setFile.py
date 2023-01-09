from assembler_algo import *


def pass1(loc_list, loc, label, opcode, operand, optab_label):
    f = open("./INTFILE", 'w')

    for i in range(len(label)):
        # loc 계산
        # 시작부분인 START일때
        if opcode[i] == 'start':
            data = f"{format(loc, 'x')}  {label[i]}     {opcode[i]}   {operand[i]}\n"
            loc_list.append(format(loc, 'x'))  # loc list에 추가해주기
            f.write(data)
            continue

        # 그 외 symbol
        if label[i] in optab_label:
            # 테이블 작성

            # format 맞추기
            if len(label[i]) == 4:
                if len(opcode[i]) == 4:
                    data = f"{format(loc, 'x')}  {label[i]}     {opcode[i]}    {operand[i]}\n"
                else:
                    data = f"{format(loc, 'x')}  {label[i]}     {opcode[i]}     {operand[i]}\n"
            else:
                if len(opcode[i]) == 4:
                    data = f"{format(loc, 'x')}  {label[i]}    {opcode[i]}    {operand[i]}\n"
                else:
                    data = f"{format(loc, 'x')}  {label[i]}    {opcode[i]}     {operand[i]}\n"
            loc_list.append(format(loc, 'x'))
            f.write(data)
            # 다음 위치 계산
            if opcode[i] == 'byte':  # opcode가 byte면
                # 해당하는 문자열 길이만큼 공간차지, c'hello'에서 hello 부분의 길이만큼 loc에 더하기 계산
                loc += len(operand[i].split("\'")[1])
            elif opcode[i] == 'resb':  # opcode가 resb라
                #  해당하는 byte만큼 공간차지, loc에 더하기 계산
                loc += int(operand[i])
            elif opcode[i] == 'resw':  # resw라면
                loc += int(operand[i])*3
            else:  # 그 외
                loc += 0x03
            # j선언, 이를 통해 해당하는 Label의 opcode를 진행함
            j = i
            # label routine이 끝날때까지
            while True:

                j += 1
                # label의 길이보다 index가 커질때
                if j >= len(label):
                    break
                if label[j] == '     ':
                    if opcode[j] == 'end':
                        data = f"{format(loc, 'x')}  {label[j]}    {opcode[j]}     {operand[j]}"
                    else:
                        if len(opcode[i]) == 4:
                            data = f"{format(loc, 'x')}  {label[j]}    {opcode[i]}    {operand[i]}\n"
                        else:
                            data = f"{format(loc, 'x')}  {label[j]}    {opcode[i]}     {operand[i]}\n"
                    loc_list.append(format(loc, 'x'))  # loc list에 추가해주기
                    f.write(data)
                    loc += 0x03
                else:
                    break
    f.close()


def pass2(loc_list, object_code, label, opcode, operand, instruction_code):
    f = open("./LISFILE", 'w')
    cal_object_code(loc_list, object_code, label,
                    opcode, operand, instruction_code)

    for i in range(len(label)):
        # loc 계산
        # 시작부분인 START일때
        if opcode[i] == 'start':
            # start object_code is null
            data = f"{loc_list[i]} {object_code[i]} {label[i]}     {opcode[i]}   {operand[i]}\n"
            f.write(data)
            continue
        # format 맞추기
        if len(label[i]) == 4:
            if len(opcode[i]) == 4:
                if len(object_code[i]) > 6:  # 목적코드 길이가 6보다 긴 경우
                    data = f"{loc_list[i]}  {object_code[i][:6]}   {label[i]}     {opcode[i]}     {operand[i]}\n      {object_code[i][6:]}\n"
                else:
                    data = f"{loc_list[i]}  {object_code[i]}   {label[i]}     {opcode[i]}    {operand[i]}\n"
            else:
                data = f"{loc_list[i]}  {object_code[i]}   {label[i]}     {opcode[i]}     {operand[i]}\n"

        else:
            if len(opcode[i]) == 4:
                # ldch, stch 예외처리
                if opcode[i] == 'ldch' or opcode[i] == 'stch':
                    data = f"{loc_list[i]}  {object_code[i]}   {label[i]}    {opcode[i]}    {operand[i][0]},{operand[i][1]}\n"
                else:
                    data = f"{loc_list[i]}  {object_code[i]}   {label[i]}    {opcode[i]}    {operand[i]}\n"
            else:
                data = f"{loc_list[i]}  {object_code[i]}   {label[i]}    {opcode[i]}     {operand[i]}\n"
        f.write(data)

    f.close()


def set_objfile(loc_list, object_code, label, opcode, operand):

    # 프로그램 길이
    # 마지막 loc 값 - 0번째 loc값
    program_length = format(int(loc_list[-1], 16) - int(loc_list[0], 16), 'x')
    body_length = format(int(loc_list[-2], 16) - int(loc_list[1], 16), 'x')

    f = open("./OBJFILE", 'w')

    for i in range(len(label)):

        # 기본 데이터
        data = ''

        # H작 record, opcode가 start라면 H
        if opcode[i] == 'START':
            start_address = operand[i]
            data = data + \
                f'H{label[i]}  {start_address.zfill(6)}{program_length.zfill(6)}\n'

            f.write(data)

        # E record
        elif opcode[i] == 'END':
            for j in range(len(label)):
                if operand[i] == label[j]:
                    data = data + f'\nE{loc_list[j].zfill(6)}\n'
                    break
            f.write(data)

        # T record
        # 최대 길이 1E : 30
        else:

            # first라면 T붙이기
            if loc_list[i] == start_address:
                # T, 레코드 시작 주소, 길이, obeject코드
                data = 'T' + \
                    start_address.zfill(
                        6) + body_length.upper() + object_code[i]
            # first 가 아니라면
            else:

                # resb만나는 경우 개행
                if opcode[i] == 'RESB' or opcode[i] == 'RESW':
                    # 다음이 끝이 아닌 경우
                    if opcode[i+1] != 'END':
                        # 끝이 아닌경우 T record 이어주기
                        data = data + '\nT'
                else:
                    # 임시데이터 저장소
                    temp_data = data + object_code[i]
                    # 오브젝트 코드 붙인 길이가 최대길이보다 길때
                    if len(temp_data) > 30:
                        # 개행하고 다음줄부터 작성
                        data = data + '\n' + 'T' + object_code[i]
                    # 최대길이보다 짧으면
                    else:
                        # data에 반영
                        data = temp_data
            f.write(data)

    f.close()
