from dictionary import symbols
from parse import *
from decode import *

# clean the asm file
clean_file('Pong.asm')

# read the cleaned file
with open('cleaned_file.txt', 'r') as c:
    lines = [line.rstrip('\n') for line in c]

num_lines = 0
for line in lines: 
    if ('(' in line):
        label = find_labels(line)
        symbols[label] = num_lines
    else:
        num_lines += 1


# now for second pass add symbols
address = 16
for line in lines:
    line = line.strip()
    if ('@' in line):
        symbol = find_symbols(line)
        print(symbol)
        if symbol.isnumeric():
            continue
        else:
            if symbol not in symbols.keys():
                symbols[symbol] = address
                address += 1
    
print(symbols)

# 3rd pass where file is generated
hack = open('Pong.hack', 'w')

for line in lines:
    line = line.strip()
    if ('(' in line):
        continue
    elif ('@' in line):
        symbol = find_symbols(line)
        print(symbol)
        if symbol.isnumeric():
            binary = convert_binary(int(symbol))
            hack.write('0' + str(binary) + '\n')
        else:
            mem_addr = symbols[symbol]
            print(mem_addr)
            binary = convert_binary(mem_addr)
            hack.write('0' + str(binary) + '\n')
    else:
        binary = translate_c_instruction(line)
        hack.write(binary + '\n')

hack.close()




