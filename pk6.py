name : Tharun kumar K R
USN  : KUB24EEE651
DATE : 21-08-2026

# numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

# even_numbers = [num for num in numbers if num % 2 == 0]

# print(even_numbers)

# text = "university"
# reverse = ""

# for char in text:
#     reverse = char + reverse

# print(reverse)

# pk6.py

# numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

# total = 0

# for num in numbers:
#     total = total + num

# average = total / len(numbers)

# print("Average =", average)

# numbers = [-1, 3, 34, -8, -9, 1]

# smallest = numbers[0]

# for num in numbers:
#     if num < smallest:
#         smallest = num

# print("Smallest number =", smallest)

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]                                                                                  
list3 = [4, 5, 6, 7]

# common = []

# for num in list1:
#     if num in list2 and num in list3:
#         common.append(num)

# print("Common elements =", common)


# numbers = [3, 10, 12, 54, 75, 89, 25, 23]

# for num in numbers:
#     if num % 3 != 0:
#         print(num)

# text = "university"

# count = 0

# for char in text:
#     count = count + 1

# print("Number of characters =", count)


# numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

# unique_numbers = list(set(numbers))
# unique_numbers.sort()

# second_smallest = unique_numbers[1]

# print("Second smallest element =", second_smallest)    


# numbers = [-1, 3, 34, -8, -9, 1]

# numbers[0], numbers[-1] = numbers[-1], numbers[0]

# print(numbers)


# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]

# repeating = []

# for num in list1:
#     if num in list2:
#         repeating.append(num)

# print("Repeating values =", repeating)

# numbers = [3, 10, 15, 54, 75, 89, 25, 23]

# for num in numbers:
#     if num % 3 == 0 and num % 5 == 0:
#         print(num)

# numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

# smallest = min(numbers)
# largest = max(numbers)

# print("Smallest:", smallest)
# print("Largest:", largest)

# numbers = [-1, 3, 34, -8, -9, 1]

# numbers[0], numbers[2] = numbers[2], numbers[0]

# print(numbers)

# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]

# non_repeating = set(list1) ^ set(list2)

# print("Non-repeating values:", non_repeating)


num = int(input("Enter a number: "))

if num % 3 == 0:
    print("Square:", num ** 2)
else:
    print("Number is not divisible by 3")




