#!/usr/bin/python3
if __name__ == "__main__":
    length = len(argv)
    added = 0
    if length == 1:
        print("{:d}",.format(0))
    if length > 1:
        for index in range(1, length):
            added += int(argv[index])
        print("{:d}".format(added))
