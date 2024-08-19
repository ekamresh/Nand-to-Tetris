(Restart)
@SCREEN
D=A
@addr
M=D // loads address of screen into memory

(KDBCheck)
@KDB 
D=M // read input of keyboard
@White
D;JEQ // make screen white if no key pressed
@Black
D;JGT // make screen black if key pressed

@KDBCheck
0;JMP

(White)
@0
M=0
@Loop
0;JMP // jump to loop now that condition is set

(Black)
@0
M=-1
@Loop
0;JMP // jump to loop now that condition is set

(Loop)
@0
D=M // read state for operation

@addr
A=M
M=D // enter value of the data register to be stored

@addr
D=M+1
@KDB
D=A-D

@addr
M=M+1

@Loop
D;JGT

@Restart
0;JMP


