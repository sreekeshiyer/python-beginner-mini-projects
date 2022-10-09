import matplotlib.pyplot as plt

n = int(input())
num = []
x_axis = []
num.insert(0, n)
while n != 1:
    if n % 2 == 0:
        n = int(n / 2)
        num.append(n)
    else:
        n = 3 * n + 1
        num.append(n)

print(len(num))
print(num)

for i in range(1, len(num) + 1):
    x_axis.append(i)

plt.xlabel("STEPS")
plt.ylabel("VALUES")
plt.plot(x_axis, num)

plt.show()


# collatz
