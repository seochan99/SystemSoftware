from getFile import *  # 파일 가져오기
from setFile import *  # 파일 쓰기

# opcode.txt
instruction = []  # 지시문
code = []  # code

# loc 아스키 코드값 (16진수) 출력을 위해 0x붙임
loc = 0x1000

# INTFILE
label = []  # label
optab_label = []  # 공백제외한 label들
opcode = []  # opcdoe
operand = []  # operand
loc_list = []  # loc_list

# LISFILE
object_code = []

# OBJFILE
t_record = []


# optab 가져오기
get_optab(instruction, code)

# instruction : code 생성
instruction_code = {}
for i in range(len(instruction)):
    instruction_code[instruction[i]] = code[i]
# print(instruction_code)

# srcfile 가져오기
get_srcfile(label, opcode, operand, optab_label)

# INTFILE 작성
# PASS1
pass1(loc_list, loc, label, opcode, operand, optab_label)

# PASS2
pass2(loc_list, object_code, label, opcode, operand, instruction_code)

# 대문자 만들기
loc_list = [i.upper() for i in loc_list]
object_code = [i.upper() for i in object_code]
label = [i.upper() for i in label]
opcode = [i.upper() for i in opcode]

# operand는 이차원리스트이므로 별도로 대문자로 만들기진행
for i in range(len(operand)):
    if len(operand[i]) == 2:
        operand[i][0] = operand[i][0].upper()
        operand[i][1] = operand[i][1].upper()
    else:
        operand[i] = operand[i].upper()

# 오브젝트 파일 만들기
set_objfile(loc_list, object_code, label, opcode, operand)

# 오브젝트 파일 읽기
get_objfile(t_record)

# t_record 문자열 합치기
t_record_data = ''
for i in range(len(t_record)):
    t_record_data = t_record_data + t_record[i]
# a 레지스터 계산
a_register = 0

# 6개씩 자르기
split_data = list(map(''.join, zip(*[iter(t_record_data)]*6)))
# t_record 요소 찾기
# for i in range(len(split_data)):
#     for j in range(len(label)):
#         # 같은것을 찾으면
#         if split_data[i][2:] == loc_list[j]:
#             for k in range(len(label)):
#                 if split_data[i] == object_code[k]:
#                     if opcode[k] == 'LDA':
#                         a_register = int(operand[j], 16)
#                     if opcode[k] == 'ADD':
#                         a_register += int(operand[j], 16)
#                     if opcode[k] == 'MUL':
#                         a_register *= int(operand[j], 16)
#                     if opcode[k] == 'SUB':
#                         a_register -= int(operand[j], 16)
# print(f"A resgier : {a_register}")

cnt = 0

print("실행 : r, 종료 : q")
cmd_cnt = int(input("한 번에 실행할 명령어 갯수 : "))

while True:
    opt = input()
    if opt == 'q':
        print("프로그램을 종료합니다.")
        break
    elif opt == 'r' and cnt < len(split_data):
        # 원하는 실행할 명령어 갯수만큼 실
        for _ in range(cmd_cnt):
            print(f"{object_code[cnt+1]} {opcode[cnt+1]} {operand[cnt+1]}")
            # 계산
            for j in range(len(label)):
                if split_data[cnt][2:] == loc_list[j]:
                    for k in range(len(label)):
                        if split_data[cnt] == object_code[k]:
                            if opcode[k] == 'LDA':
                                a_register = int(operand[j], 16)
                            elif opcode[k] == 'ADD':
                                a_register += int(operand[j], 16)
                            elif opcode[k] == 'MUL':
                                a_register *= int(operand[j], 16)
                            elif opcode[k] == 'SUB':
                                a_register -= int(operand[j], 16)
                            else:
                                break
            print(f"REGISTER A : {a_register}\n")
            # cnt증가
            cnt += 1
    else:
        print("r 또는 q를 입력해주세요.")
