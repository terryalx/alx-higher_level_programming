#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    n = sys.argv[1:]
    e = len(n)
    if e == 0:
        print("0 arguments.")
    for i in n:
        print (len(n), "arguments:")
        break
    z = 1
    for i in n:
        print(f"{z}: {i}")
        z += 1

