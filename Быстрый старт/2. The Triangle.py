def main():
    a = int(input())
    b = int(input())
    c = int(input())

    if (a*a <= b*b + c*c) and (b*b <= a*a + c*c) and (c*c <= a*a + b*b):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()