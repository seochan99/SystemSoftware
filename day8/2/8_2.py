# 파일 오픈
f = open("./SRCFILE", 'r')

# label, opcode, operand list
label = []
opcode = []
operand = []

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
        opcode.append(temp[1])
        operand.append(temp[2])

# close file
f.close()

# print label, opcode, oeprand
for i in range(len(label)):
    print(f"Label: {label[i]}, Opcode: {opcode[i]}, Operand: {operand[i]}")
