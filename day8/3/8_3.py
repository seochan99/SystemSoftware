# 파일 오픈
f = open("./SRCFILE", 'r')

# label, opcode, operand list
label = []
optab_label = []
opcode = []
operand = []

# loc 아스키 코드값 (16진수) 출력을 위해 0x붙임
loc = 0x1000


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


# print label, opcode, oeprand
# word : 3byte
# byte : 1byte

# flag,
flag = {}
for i in label:
    try:
        flag[i] += 1
    except:
        flag[i] = 0
# print(flag)

# 시작부분인 test일때
if label[0] == 'test':
    print(
        f"Label: {label[0]}, Loc: {format(loc, 'x')}, flag: {flag[f'{label[0]}']}")

for i in range(1, len(label)):
    # 그 외 symbol
    if label[i] in optab_label:
        # Label 출력
        print(
            f"Label: {label[i]}, Loc: {format(loc, 'x')}, flag: {flag[f'{label[i]}']}")
        # 다음 위치 계산
        if opcode[i] == 'byte':  # opcode가 byte면
            # 해당하는 문자열 길이만큼 공간차지, c'hello'에서 hello 부분의 길이만큼 loc에 더하기 계산
            loc += len(operand[i].split("\'")[1])
        elif opcode[i] == 'resb':  # opcode가 resb라
            #  해당하는 byte만큼 공간차지, loc에 더하기 계산
            loc += int(operand[i])
        else:  # 그 외
            loc += 0x03
        # j선언, 이를 통해 해당하는 Label의 opcode를 진행함
        j = i
        # label routine이 끝날때까지
        while True:
            j += 1
            if j >= len(label):
                break
            if label[j] == '-    ':
                loc += 0x03
            else:
                break
    # 그외 부분
