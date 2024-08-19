def find_labels(line):
    #chars = ['(', ')']
    line = line.replace('(', '').replace(')', '')
    return line

def find_symbols(line):
    line = line.replace('@', '')
    return line


def remove_comments(line):
    parts = line.split('//', 1)
    return parts[0].rstrip()


# remove whitespace and comments
def clean_file(fname):
    # open file and create new file to 
    assembly = open(fname, 'r')
    cleaned_file = open('cleaned_file.txt', 'w')

    # iterate through file - only store content
    lines = assembly.readlines()

    for i, line in enumerate(lines):
        if line.strip():
            new_line = remove_comments(line)
            if (new_line != ""):
                if i == len(lines) - 1:
                    cleaned_file.write(new_line)
                else:
                    cleaned_file.write(new_line + '\n')


def convert_binary(num):
    mem_addr_bin = bin(num)[2:]
    #print(mem_addr_bin)
    binary = mem_addr_bin.zfill(15)
    #print(binary)
    return binary 

def convert_binary_label(num):
    mem_addr_bin = bin(num)[2:]
    #print(mem_addr_bin)
    binary = mem_addr_bin.zfill(16)
    #print(binary)
    return binary 
