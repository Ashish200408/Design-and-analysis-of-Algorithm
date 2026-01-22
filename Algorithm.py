'''Write a program to check if a number is even or odd(done)
Create a python function that returns the square of a number (done)
Write a python program to find the largest of three numbers (done)
Write a python program to calculate the sum of all the elements in a list (done)
Write a python program to reverse a string (done)
Write a program to check if a given word is a palindrome (done)
Write the program to find the factorial of a number using recursion
write a program to check if the given number is a prime number
write a program for sequential search'''

'''num= int(input("Enter a number: "))
if num % 2==0:
    print("Even")
else:
    print("odd")'''


'''a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
if a>b & a>c:
    print("a is largest number")
elif b>a & b>c:
    print("b is largest number")
else: 
    print("c is largest number")'''


'''numbers = [1, 2, 4, 8, 9]
total = 0

for num in numbers:
    total += num

print(total)'''


'''a="Ashish"
for i in range (len(a)-1,-1,-1):
    print(a[i],end="")'''


'''word = input("Enter a word: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")'''


'''def square(n):
    return n * n

print(square(8))'''

'''num = int(input("Enter a number: "))

if num <= 1:
    print("Not a Prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime number")
            break
    else:
        print("Prime number")'''


'''arr = [10, 25, 30, 45, 60]
key = int(input("Enter element to search: "))

found = False

for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at index", i)
        found = True
        break

if not found:
    print("Element not found")'''


'''def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))'''











