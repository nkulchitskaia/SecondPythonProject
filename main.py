n = int(input())
a = input()
counter = 0
for i in a.split():
    if int(i) > 0:
        counter += 1
print(counter)


