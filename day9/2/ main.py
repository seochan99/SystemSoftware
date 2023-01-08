from getFile import *  # 파일 가져오기
from setFile import *  # 파일 쓰기

# opcode.txt
instruction = []  # 지시문
code = []  # code

# loc 아스키 코드값 (16진수) 출력을 위해 0x붙임
loc = 0x1000

# srcfile
label = []  # label
optab_label = []  # 공백제외한 label들
opcode = []  # opcdoe
operand = []  # operand

# optab 가져오기
get_optab(instruction, code)
# srcfile 가져오기
get_srcfile(label, opcode, operand, optab_label)
# INTFILE 작성
set_intfile(loc, label, opcode, operand, optab_label)
print(label)
