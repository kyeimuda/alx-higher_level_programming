#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    from sys import argv
    length = len(argv)
    value1 = int(argv[1])
    value2 = int(argv[3])
    if length != 4:
        print("""Usage: ./100-my_calculator.py <a> <operator> <b>""")
        exit(1)
    elif argv[2] != '+' or argv[2] != '-' or argv[2] != '*' or argv[2] != '/':
        print("""Unknown operator. Available operators: +, -, * and /""")
        exit(1)
    elif argv[2] == '+':
        print("{:d} + {:d} = {:d}".format(value1, value2, calculator_1.add(value1, value2)))
    elif argv[2] == '-':
        print("{:d} + {:d} = {:d}".format(value1, value2, calculator_1.sub(value1, value2)))
    elif argv[2] == '*':
        print("{:d} + {:d} = {:d}".format(value1, value2, calculator_1.mul(value1, value2)))
    elif argv[2] == '/':
        print("{:d} + {:d} = {:d}".format(value1, value2, calculator_1.div(value1, value2)))
