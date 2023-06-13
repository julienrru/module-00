import sys

print(sys.argv)

def reverse_and_swap_case(string):
    reversed_string = string[::-1]
    swapped_case_string = reversed_string.swapcase()
    return swapped_case_string

if len(sys.argv) > 1:
    arguments = ' '.join(sys.argv[1:])
    result = reverse_and_swap_case(arguments)
    print(result)
else:
    print("Usage: python program.py [string1] [string2] ...")


