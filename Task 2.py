x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [37, 74, 135, 226, 353, 531, 739, 1010, 1341, 1738]

def difference_table(y):
    table = [y[:]]

    for i in range(1, len(y)):
        differences = []

        for j in range(len(table[i - 1]) - 1):
            differences.append(table[i - 1][j + 1] - table[i - 1][j])

        table.append(differences)

    return table


table = difference_table(y)

print("Original Difference Table")
print("x\tf(x)\tΔ1\tΔ2\tΔ3\tΔ4")

for i in range(len(x)):
    print(f"{x[i]}\t{y[i]}", end="")

    for j in range(1, 5):
        if i < len(table[j]):
            print(f"\t{table[j][i]}", end="")

    print()

third = table[3]

print("\nThird Differences:", third)

for i in range(len(third) - 1):
    if third[i] != third[i + 1]:
        print("\nError detected!")
        print("Erroneous value:", y[5])
        print("Error is at x =", x[5])

        y[5] = 522

        print("Corrected value:", y[5])
        break


table = difference_table(y)

print("\nCorrected Difference Table")
print("x\tf(x)\tΔ1\tΔ2\tΔ3\tΔ4")

for i in range(len(x)):
    print(f"{x[i]}\t{y[i]}", end="")

    for j in range(1, 5):
        if i < len(table[j]):
            print(f"\t{table[j][i]}", end="")

    print()