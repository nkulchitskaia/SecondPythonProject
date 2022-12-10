if __name__ == "__main__":
    n = int(input())
    a = input()
    for i in range(n):
        if i % 2 == 0:
            print(a.split()[i], end=' ')