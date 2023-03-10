def get_optab(instruction, code):
    # optab저장
    f = open("./optab.txt", 'r')
    while True:
        line = f.readline()
        if not line:                                # 파일 읽기 스탑
            break
        # 개행 없애고 공백기준 split하여 List화 하여 temp에 임시 저장
        temp = line.rstrip('\n').split()
        # temp[0] : instruction, temp[1] : code이므로 각각의 list에 저장
        instruction.append(temp[0])
        code.append(temp[1])
    # 파일 닫기
    f.close()


def get_srcfile(label, opcode, operand, optab_label):
    # 파일 오픈
    # file_name = input('파일 이름 입력 : ')
    file_name = 'srcfile'

    # srcfile 입력받기
    try:
        f = open(f"./{file_name}", 'r')
    except:
        print(f"[ERROR] '{file_name}' File Not Found")
        exit()
    # 파일 정보 저장
    while True:
        line = f.readline()
        if not line:                                # 파일 읽기 스탑
            break
        # 개행 없애고 공백기준 split하여 List화 하여 temp에 임시 저장
        temp = line.rstrip('\n').split()
        # label이 없는 경우 temp의 len은
        if len(temp) == 2:
            # temp[0] : opcode
            # temp[1] : operand이므로 각각의 list에 저장
            label.append('     ')
            opcode.append(temp[0])
            operand.append(temp[1])
        elif len(temp) == 3:
            # temp[0] : label
            # temp[1] : opcode
            # temp[2] : operand이므로 각각의 list에 저장
            label.append(temp[0])
            optab_label.append(temp[0])
            opcode.append(temp[1])
            operand.append(temp[2])
    # close file
    f.close()


def get_objfile(t_record):
    # optab저장
    f = open("./objfile", 'r')
    cnt_t = 0
    while True:
        # 한줄 읽는다
        line = f.readline()
        if not line:                                # 파일 읽기 스탑
            break
        # 개행 없애고 공백기준 split하여 List화 하여 temp에 임시 저장
        # 시작주소, 길이,
        # T record라면 cnt t 1상승
        if line[0] == 'T':
            cnt_t += 1
            # T record의 첫줄이라면
            if cnt_t == 1:
                # 시작주소, 길이 날리기 = 1 + 6 + 2
                # index 10부터 시작
                # 9개 날림
                t_record.append(line[9:].rstrip('\n'))
            else:
                t_record.append(line[1:].rstrip('\n'))
    # 파일 닫기
    f.close()
