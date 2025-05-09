#Question 1
a,b,c=map(int,input("Enter number : ").split())
print(max(a,b,c))

#Qestion 2
n=10
for i in range(1,n+1):
    print(2*i,end='')

#Question 3
a,b=map(int,input("enter operands : ").split())
op=input("enter operator (+,-,*,/): ")
if op=='+':
    print("Addition",a+b)
elif op=='-':
    print("Subtract",a-b)
elif op=='*':
    print("multiply",a*b)
else :
    if b==0
        print("not divisible")
    else :
        print("divide",a/b)

#Question 4
n=int(input("enter number : "))
pr=True
if n>2:
    for i in range(2,n):
        if n%i==0:
            pr=False
            break
    if pr :
        print("Number is prime")
    else:
        print("Not prime")

#Queston 5
n = int(input("Enter number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

#Question 6
num = int(input("Enter a number: "))
total = 0
while num > 0:
    total += num % 10
    num //= 10
print("Sum of digits:", total)

#Question 7
num = int(input("Enter a number: "))
count = 0
if num == 0:
    count = 1
while num > 0:
    num //= 10
    count += 1
print("Number of digits:", count)

#Question 8
n = int(input("Enter number of rows (half of diamond): "))
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

#Question 9
while True:
    num = input("Enter a number greater than 0: ")
    if num.isdigit() and int(num) > 0:
        print("Valid input:", num)
        break
    print("Invalid input. Try again.")

#Question 10
total = 0
for i in range(100):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print("Sum:", total)


