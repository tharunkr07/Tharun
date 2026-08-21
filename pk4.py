number = [10, 20, 30, 40, 50]
target = 40
middle = 30
for i in range(len(number)):
    if i < middle:
        if number[i] == target:
          print("number Found at index", i)
    else:
        print("number not Found")