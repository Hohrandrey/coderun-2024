def main():
    list = input().split()
    count = 0
    for i in range(1, len(list)-1):
        if int(list[i-1]) < int(list[i]) and (int(list[i]) > int(list[i+1])):
            count+=1
    print(count)

if __name__ == '__main__':
    main()