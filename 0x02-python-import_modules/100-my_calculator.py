#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])
    result = 0
    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = sub(a, b)
    elif op == '*':
        result = mul(a, b)
    elif op == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{} {} {} = {}".format(a, op, b, result))
    sys.exit(0)
