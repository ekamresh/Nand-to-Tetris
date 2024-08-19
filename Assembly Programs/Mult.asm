@1
D=M
@END
D;JEQ
@temp
M=D

@0
D=M
@END
D;JEQ
@temp2
M=D

@2
M=0

(LOOP)
@temp
D=M
@2
M=D+M

@temp2
M=M-1
D=M

@LOOP
D;JGT

(END)
@END
0;JMP
