
def set_intfile(loc, label, opcode, operand, optab_label):
    f = open("./INTFILE", 'w')

    for i in range(len(label)):
        # loc 계산
        # 시작부분인 START일때
        if opcode[i] == 'start':
            data = f"{format(loc, 'x')}  {label[i]}     {opcode[i]}   {operand[i]}\n"
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
            f.write(data)
            # 다음 위치 계산
            if opcode[i] == 'byte':  # opcode가 byte면
                # 해당하는 문자열 길이만큼 공간차지, c'hello'에서 hello 부분의 길이만큼 loc에 더하기 계산
                loc += len(operand[i].split("\'")[1])
            elif opcode[i] == 'word':
                loc += len(operand[i].split("\'")[1])*3
            elif opcode[i] == 'resb':  # opcode가 resb라
                #  해당하는 byte만큼 공간차지, loc에 더하기 계산
                loc += int(operand[i])
            elif opcode[i] == 'resw':
                loc += int(operand[i]*3)
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
                    f.write(data)
                    loc += 0x03
                else:
                    break
