import sys
sys.stdin = open("azs.txt")
azs_info = dict()
azs_status = dict()
status = dict()
while True:
    try:
        line = input()
        azs_info[line[0]] = [line[2], line[4:], 0]
        azs_status[line[0]] = []
        if line == '':
            break
    except (ValueError, EOFError):
        break
