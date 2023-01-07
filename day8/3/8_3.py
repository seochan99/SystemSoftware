# 파일 오픈
f = open("./SRCFILE", 'r')

# label, opcode, operand list
label = []
optab_label = []
opcode = []
operand = []

# loc 아스키 코드값 (16진수) 출력을 위해 0x붙임
loc = 0x1000
# falg 0으로 초기화
flag = 0


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
        label.append('-    ')
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

# 시작부분인 test일때
if label[0] == 'test':
    print(f"Label: {label[0]}, Loc: {format(loc, 'x')}, flag: {flag}")


# print label, opcode, oeprand
# word : 3byte
# byte : 1byte

for i in range(1, len(label)):
    # 그 외 symbol
    if label[i] in optab_label:
        print(f"Label: {label[i]}, Loc: {format(loc, 'x')}, flag: {flag}")
        loc += 0x03
        j = i
        while True:
            j += 1
            if j >= len(label):
                break
            if label[j] == '-    ':
                loc += 0x03
            else:
                break
    # 그외 부분
