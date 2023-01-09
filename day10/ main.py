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
loc_list = []

# LISFILE
object_code = []

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
