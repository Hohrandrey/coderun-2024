import sys


def main():
    n = int(sys.stdin.readline())
    dict = {}
    for n in range(n):
        stri = input()
        dict[n] = stri
    sp = []
    for i in range(0, len(dict)):
        for j in range(1, len(dict)):
            c = 0
            res = dict[i] + dict[j]
            if len(res)%2 ==0:
                for x in range(len(res)//2):
                    if res[x] == res[len(res)-1-x]:
                        c +=1
            if c == len(res)/2:
                sp.append((i, j))
    print(sp)




if __name__ == '__main__':
    main()