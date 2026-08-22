NAME : THARUN KUMAR K.R
USN  : KUB25EEE651
DATE : 22/08/2026


nums = [3, 10, 15, 54, 75, 25, 23]

found = False

for num in nums:
    if num % 3 == 0 and num % 5 == 0 and num % 8 == 0:
        print(num)
        found = True

if not found:
    print("none")


nums = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

smallest_index = nums.index(min(nums))
largest_index = nums.index(max(nums))

nums[smallest_index], nums[largest_index] = nums[largest_index], nums[smallest_index]

print(nums)


nums = [-1, 3, 34, -8, -9, 1]

nums[nums.index(-1)] = 100

print(nums)

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

average1 = sum(list1) / len(list1)
average2 = sum(list2) / len(list2)

print("Average of list 1:", average1)
print("Average of list 2:", average2)


num = int(input("Enter a number: "))

if num % 3 == 0:
    num = num + 5

print(num)

nums = [3, 10, 15, 54, 75, 25, 23]

for num in nums:
    if num % 3 == 0 and num % 5 != 0:
        print(num)

nums = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

for num in nums:
    if num > 20:
        print(num)

nums = [-1, 3, 34, -8, -9, 1]

for num in nums:
    if num < 0:
        print(num)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

count = len(nums)

print("Count:", count)

num = int(input("Enter a number: "))

if num % 3 == 0:
    num = num * 5

print(num)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

total = num1 + num2

if total % 5 == 0:
    print("The sum is divisible by 5")
else:
    print("The sum is not divisible by 5")

numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

prime_numbers = []

for num in numbers:
    if num < 2:
        continue

    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        prime_numbers.append(num)

print("Prime numbers:", prime_numbers)


numbers = [-1, 3, 34, -8, -9, 1]

print("Original list:", numbers)

numbers.append(10)
print("After append:", numbers)

numbers.insert(2, 20)
print("After insert:", numbers)

numbers.remove(-8)
print("After remove:", numbers)

numbers.sort()
print("After sorting:", numbers)

numbers.reverse()
print("After reversing:", numbers)

print("Length of list:", len(numbers))

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

print("Sum:", sum(numbers))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

total = sum(numbers)
average = total / len(numbers)

print("Average of the list:", average)


number = 1578693
divisors = []

for i in range(1, 11):
    if number % i == 0:
        divisors.append(i)

print("Divisors that divide", number, "are:", divisors)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 % 5 == 0:
    print("Square of", num1, "is", num1 ** 2)
else:
    print(num1, "is not divisible by 5")

if num2 % 5 == 0:
    print("Square of", num2, "is", num2 ** 2)
else:
    print(num2, "is not divisible by 5")

numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

prime_numbers = []
even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)


    if num > 1:
        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers.append(num)

print("Prime numbers:", prime_numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)


numbers = [-1, 3, 34, -8, -9, 1]

result = []

for num in numbers:
    if num >= 0 and num % 3 != 0:
        result.append(num)

print("After removing negative numbers and numbers divisible by 3:", result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

total = sum(numbers)
count = len(numbers)
average = total / count

print("Sum:", total)
print("Count:", count)

number = 1578693

for divisor in range(1, 11):
    if number % divisor == 0:
        print(number, "is divisible by", divisor)
        number = number - 100
    else:
        print(number, "is not divisible by", divisor)

print("Final number:", number)

word = "university"
vowels = "aeiou"

count = 0

for char in word:
    if char in vowels:
        count += 1

print("Number of vowels:", count)

numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

print(numbers[12])

numbers.insert(9, 59)

print(numbers)

numbers = [-1, 3, 34, -8, -9, 1]

squares = []

for num in numbers:
    squares.append(num ** 2)

print(squares)


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 // num2

print("Floor division:", result)

numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89, 7, 8, 54, 621, 57, 24, 3, 5, 6, 4]

unique_values = []

for num in numbers:
    if num not in unique_values:
        unique_values.append(num)

print(unique_values)