n = int(input("Enter a number:"))
num = len(str(abs(n)))
sum = 0
t = n
while n > 0:
    rem = n % 10
    x = rem**num
    sum = sum + x
    n = n // 10

if t == sum:
    print(f"{t} is an Armstrong number")
else:
    print(f"{t} is not an Armstrong number")

