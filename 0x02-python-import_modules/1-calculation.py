#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as work
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, work.add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, work.sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, work.mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, work.div(a, b)))
