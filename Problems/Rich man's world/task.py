initial_sum = int(input())
i = 0
while initial_sum < 700000:
    initial_sum += initial_sum * 7.1 / 100
    i += 1
print(i)
