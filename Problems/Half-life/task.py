initial = int(input())
final = int(input())
i = 0
while final < initial:
    i += 1
    initial = initial / 2
print(i * 12)