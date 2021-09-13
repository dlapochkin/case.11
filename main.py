def main():
    time(1)
def time(t):
    if t>1445:
        return 0
    with open('input.txt') as f_in:
        print(new_client(f_in, time))
    time(t+1)
def new_client(f_in, time):
    s = list(f_in.readline().split())
    return s
main()