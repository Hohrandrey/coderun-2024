def main():
    pass

if __name__ == '__main__':
    main()

"""
#говнокод
def t(i):
    total = 0
    if i == 1 or i == 2:
        total += 1
    else:
        total += (t(i - 1) + t(i - 2))
    return total

def main():
    i = int(input())
    res = 0
    for x in range(i):
        res += t(x+1)
    print(res)



if __name__ == '__main__':
    main()
"""