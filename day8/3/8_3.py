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

# flag
flag = {}
# label을 i로 가져온다
for i in label:
    # 이미 0으로 초기화 되어 있다면 try가 실행되어 1의 값을 할당한다
    try:
        # flag는 중복여부 이므로 1이라면 중복인것을 확인한거니 패스하고
        # 1이 아니라면 중복확인한것이 아니니 확인해준다.
        if flag[i] != 1:
            flag[i] = 1
    # except 문이 수행되면 0으로 초기화 된다.
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
            # label의 길이보다 index가 커질때
            if j >= len(label):
                break
            if label[j] == '-    ':
                loc += 0x03
            else:
                break
