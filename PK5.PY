# numbers = [12, 7, 22, 15, 40, 33, 56, 91, 100]
# divisible_by_two = [num for num in numbers if num % 2 == 0]
# print("Numbers divisible by 2:", divisible_by_two) 

# my_list = [10, 20, 30, 40, 50, 60, 70]
# print("Original list: ", my_list)
# my_list.insert(6, "Value_at_6")
# my_list.insert(4, "Value_at_4")
# print("Modified list: ", my_list)

# my_list = [10, 20, 30, 40, 50]
# my_list.reverse()
# print(my_list)


# my_dict = {"name": "Alice", "age": 25, "city": "New York"}
# print(my_dict)

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):

#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
                
# numbers = [5,3,4,1]
# bubble_sort(numbers)
# print(numbers)

# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
        
# numbers = [5, 3, 4,1]
# selection_sort(numbers)
# print(numbers)

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key
            
# numbers = [5, 3, 4,1]
# insertion_sort(numbers)
# print(numbers)
        
        
# def find_smallest(numbers):
#     if not numbers:
#         return "The list is empty"
#     smallest = numbers[0]
#     for num in numbers:
#         if num < smallest:
#             smallest = num 
#     return smallest
# my_list = [18, 45, 3, 92, 5, 27]
# result = find_smallest(my_list)
# print("The smallest number is:", result)
        
        
# def linear_search(arr, target):
#     for index in range(len(arr)):
#         if arr[index] == target:
#             return index 
            
#     return -1
# numbers = [10, 50, 30, 70, 80, 20, 90, 40]
# target_value = 30

# result = linear_search(numbers, target_value)

# if result != -1:
#     print(f"Target found at index: {result}")
# else:
#     print("Target not found in the list.")


# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1
# sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
# target_value = 23

# result = binary_search(sorted_list, target_value)

# if result != -1:
#     print(f"Element found at index: {result}")
# else:
#     print("Element not found in the list")


# def single_bubble_sort_pass(arr):
#     n = len(arr)
#     for j in range(0, n - 1):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
            
#     return arr

# initial_list = [5, 2, 4, 1]
# result = single_bubble_sort_pass(initial_list)
# print("Li
      
# stack = []
# stack.append(10)
# stack.append(20)
# stack.append(30)

# print(stack)

# item = stack.pop()
# print(item)
# print(stack)

# queue = []
# queue.append("tharun")
# queue.append("anji")
# queue.append("samantha")

# person = queue.pop(0)

# print(person)
# print(queue)

# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")
  
# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")
    
# x = 5
# y = 10
# print(f"Before: x = {x}, y = {y}")
# x, y = y, x

# print(f"After: x = {x}, y = {y}")

# Python program to find the second largest number
# without using max() or sorted()

# numbers = list(range(1, 21))

# even_numbers = [num for num in numbers if num % 2 == 0]

# print("List:", numbers)
# print("Even numbers:", even_numbers)
# print("Count of even numbers:", len(even_numbers))

# numbers = [10, 5, 8, 2, 15, 3]

# smallest = min(numbers)

# print("Smallest number:", smallest)

# number = int(input("Enter a number: "))
# divisor = int(input("Enter the divisor: "))

# if number % divisor == 0:
#     print("The number is divisible by the divisor.")
# else:
#     print("The number is not divisible by the divisor.")
    

# numbers = list(range(1, 21))

# reverse_numbers = numbers[::-1]

# print("Original list:", numbers)
# print("Reversed list:", reverse_numbers)


# numbers = [10, -5, 3, -1, 7, 0, -2, 8]

# positive_numbers = [num for num in numbers if num > 0]

# print("Positive numbers:", positive_numbers)

# numbers = [100, -5, 32, -100, 750, 0, -2, 81]

# sum_positive = 0

# for num in numbers:
#     if num > 0:
#         sum_positive += num

# print("Sum of positive numbers:", sum_positive)


# numbers = [100, -5, 32, -100, 750, 0, -2, 81]

# count = 0

# for num in numbers:
#     if num > 10:
#         count += 1

# print("Count of numbers greater than 10:", count)

# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# total = 0

# for num in numbers:
#     total += num

# average = total / len(numbers)

# print("Average:", average)

# list = [10, 15, 22, 31, 40, 47, 56, 63, 78, 85]

# even = []
# odd = []
    
# for num in list:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)

# print("Even numbers:", even)
# print("Odd numbers:", odd)


# numbers = [10, 15, 22, 31, 40, 47, 56, 63, 78, 85]

# count = 0

# for num in numbers:
#     if num % 5 == 0:
#         count += 1

# print("Count of numbers divisible by 5:", count)


# list = [10, -5, 3, -1, 7, 0, -2, 8]
# index = list.index(0)
# print(index)

# list = [100, -5, 32, -100, 750, 0, -2, 81]

# length = len(list)

# print(length)


# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# new_list = [list1[i] + list2[i] for i in range(10)]

# print(new_list)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_numbers = []

# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num) 
# print("Even numbers:", even_numbers)

# list = [10, 23, 33, 40, 58, 67, 72, 81, 90, 100]

# list[6] = 75

# print(list)


# def reverse_string(s):
#     return s[::-1]

# text = "Hello, world"
# reversed_text = reverse_string(text)
# print(reversed_text)


# text = "Artificialintelligence"

# count = len(text)

# print("Number of characters:", count)


# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# sum = num1 + num2

# print("Sum:", sum)



# my_list = [10, 20, 30, 40]

# print("Original list:", my_list)

# my_list.insert(2, 25)
# print("After insert():", my_list)

# my_list.append(50)
# print("After append():", my_list)

# my_list.remove(20)
# print("After remove():", my_list)

# student = {
#     "name": "Anji",
#     "age": 20,
#     "course": "Maths"
# }

# print("Original dictionary:", student)

# student["city"] = "Ballari"
# print("After adding:", student)

# student["age"] = 21
# print("After updating:", student)

# del student["course"]
# print("After deleting:", student)

# string1 = "hello, world"
# string2 = "how are you?"

# result = string1 + " " + string2

# print(result)




# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#            11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# even_count = 0
# odd_count = 0

# for num in numbers:
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# print("Number of even numbers:", even_count)
# print("Number of odd numbers:", odd_count)



# num1 = float(input("Enter first number: "))
# operator = input("Enter operator (+, -, *, /): ")
# num2 = float(input("Enter second number: "))
    
# if operator == "+":
#     result = num1 + num2
# elif operator == "-":
#     result = num1 - num2
# elif operator == "*":
#     result = num1 * num2
# elif operator == "/":
#     if num2 != 0:
#         result = num1 / num2           
#     else:
#         result = "Cannot divide by zero"
# else:
#     result = "Invalid operator"

# print("Result:", result)


# numbers = [1, 0, 5, 0, 8, 3, 0]

# non_zero = [x for x in numbers if x != 0]

# print(non_zero)


# numbers = [-2, 5, -7, 8, 3, -1, 0]

# even = []
# odd = []

# for num in numbers:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)

# print("Even numbers:", even)
# print("Odd numbers:", odd)


# numbers = [10, 5, 20, 8]

# numbers.sort()

# print(numbers)


# list1 = [1, 2, 2, 3, 4]
# list2 = [2, 2, 4, 5]
# list3 = [1, 2, 3, 4, 5]

# duplicates = []

# for num in list1:
#     if num in list2 and num in list3 and num not in duplicates:
#         duplicates.append(num)

# print(duplicates)


# numbers = input("Enter numbers separated by space: ").split()

# even = []
# odd = []

# for num in numbers:
#     num = int(num)

#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)

# print("Even numbers:", even)
# print("Odd numbers:", odd)


# num = int(input("Enter a number: "))

# numbers = []

# if num % 2 == 0 and num % 5 == 0:
#     numbers.append(num)
# print(numbers)


numbers = list(map(int, input("Enter numbers: ").split()))

print("Original list:", numbers)

numbers.append(10)
print("After append:", numbers)

numbers.insert(1, 20)
print("After insert:", numbers)

numbers.remove(10)
print("After remove:", numbers)

numbers.sort()
print("After sort:", numbers)

numbers.reverse()
print("After reverse:", numbers)

print("Length:", len(numbers))

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
