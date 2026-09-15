import math
x = []
y = []

for i in range(10, 17):
    x.append(i)
    y.append(round(math.sqrt(i**2 + i + 1), 4))

table = [y]

for i in range(1, 5):
    differences = []

    for j in range(len(table[i - 1]) - 1):
        differences.append(
            round(table[i - 1][j + 1] - table[i - 1][j], 4)
        )

    table.append(differences)

print("Difference Table")
print("x\tf(x)\tΔ1\tΔ2\tΔ3\tΔ4")

for i in range(len(x)):
    print(f"{x[i]}\t{y[i]:.4f}", end="")

    for j in range(1, 5):
        if i < len(table[j]):
            print(f"\t{table[j][i]:.4f}", end="")

    print()