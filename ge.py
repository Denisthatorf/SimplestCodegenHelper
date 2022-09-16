import os
import re

input_fullpath = "/home/denis/Projects/Python/CodeGenerator/eventCallback.hpp"
out_fullpath = "/home/denis/Projects/Python/CodeGenerator/eventCallback.out.hpp"

def is_repeat_start(line) -> bool:
    key = re.search("\s*%%repeat\s*", line)
    if key:
        return True
    else: 
        return False

def is_repeat_end(line) -> bool:
    key = re.search("\s*%%end\s*", line)
    if key:
        return True
    else: 
        return False


def parse_line(outFile, line, names):
    vars = re.findall("(?<=\$\$)(\w+)", line) 
    for varname in vars:
        line = re.sub("\$\${}".format(varname), names[varname], line) 

    outFile.write(line)
    outFile.write("\n")


def parse_repeat(outFile, lines, names_list):
    #check where end is
    end_position = -1
    for position, line in enumerate(lines):
        if is_repeat_end(line):
            end_position = position
    
    if end_position == -1:
        raise Exception("Repeat is not ended")

    #generate
    for names in names_list:
        for line in lines[:end_position]:
            parse_line(outFile, line, names)
    
    return lines[end_position + 1:]


def parse_loop(outFile, lines, names_list):
    isNotAll = True
    while isNotAll :
        for position, line in enumerate(lines):
            if is_repeat_start(line):
                lines = parse_repeat(outFile, lines[position + 1:], names_list)
                isAll = len(lines) != 0
                break
            else:
                outFile.write(line)
                outFile.write("\n")

                if position + 1 >= len(lines):
                    isNotAll = False


def parse(inFilePath, outFilePath, names_list, mode = "w"):
    #File in string lines
    inFile = open(inFilePath, "r")
    fileContent = inFile.read()
    lines = fileContent.split("\n")
    inFile.close()

    outFile = open(outFilePath, mode)
    parse_loop(outFile, lines, names_list)
    outFile.close()


def main():
    names_list = [
        { 
            "return_type" : "int",
            "input_args" : "float x, float y",
            "input_types" : "_float_float",
            "params" : "x, y"
        },
        { 
            "return_type" : "int",
            "input_args" : "double x, double y",
            "input_types" : "_double_double",
            "params" : "x, y"
        },
        { 
            "return_type" : "int",
            "input_args" : "int x, int y",
            "input_types" : "_int_int",
            "params" : "x, y"
        }
    ]

    parse(input_fullpath, out_fullpath, names_list)


if __name__ == "__main__":
    main() 