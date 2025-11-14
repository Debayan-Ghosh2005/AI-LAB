n = int(input("Enter the size of the square matrix (n): "))
a = []
for i in range(n):
    row = []
    for j in range(n):
        num = int(input(f"Enter number for position ({i}, {j}): "))
        row.append(num)
    a.append(row)
elements = [num for row in a for num in row]


if len(elements) != len(set(elements)) or any(num <= 0 for num in elements):
    print(" Not a magic square — duplicate or non-positive numbers found.")
    exit()


print("The entered matrix is:")
for i in range(n):
    for j in range(n):
        print(a[i][j], end=" ")
    print() 

magic_sum = sum(a[0])


for i in range(n):
    if sum(a[i]) != magic_sum:
        print(" Not a magic square — row sums are not equal.")
        exit()


for j in range(n):
    col_sum = sum(a[i][j] for i in range(n))
    if col_sum != magic_sum:
        print(" Not a magic square — column sums are not equal.")
        exit()
main_diag = sum(a[i][i] for i in range(n))
if main_diag != magic_sum:
    print("Not a magic square — main diagonal sum is incorrect.")
    exit()
sec_diag = sum(a[i][n - i - 1] for i in range(n))
if sec_diag != magic_sum:
    print("Not a magic square — secondary diagonal sum is incorrect.")
    exit()

print("It is a magic square!")
print("Magic constant (sum) =", magic_sum)
