n = int(input("Enter a number:"))
sum = 0
t = n
while(n>0):
    rem = n % 10
    sum = sum * 10 + rem
    n = n//10
print(sum)
if t == sum:
    print(f"{t} is a palindrome number")
else:
    print(f"{t} is not a palindrome number")