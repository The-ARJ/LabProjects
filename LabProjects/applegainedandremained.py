"""3. N students  take k apples and distribute them among each other evenly.
The remaining (the non divisible) part remains in the basket . How many apples will each single student get?
How many apples will remain in the basket? The program reads the numbers N and K. It should print the two answers for
the question above."""

N = int(input("enter a number of students:"))
K = int(input("enter a number of apples:"))
y = K%N
z = K//N
print("apples remains in basket:", y)
print("apple gain by each student:", z)