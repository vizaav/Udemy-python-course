# Write your code below this row 👇
total = 0
for i in range(2, 101, 2):
    total += i
print(total)

total2 = 0
for i in range(1, 101):
    if i % 2 == 0:
        total2 += i
print(total2)
