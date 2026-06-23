
# TASK W

def devideArray(arr, size):
    result = []

    for i in range(0, len(arr), size):
        result.append(arr[i:i + size])

    return result


# Test
print(devideArray([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))


# TASK V

# def countLetters(word):
#     result = {}

#     for letter in word:
#         if letter in result:
#             result[letter] += 1
#         else:
#             result[letter] = 1

#     return result


# print(countLetters("restaurantController"))


# TASK T
# def mergeSortedArrays(arr1, arr2):
#     return sorted(arr1 + arr2)


# print(mergeSortedArrays([0, 3, 4], [4, 6, 7]))


# TASK S

# def missingNumber(arr):
#     n = len(arr)
#     for i in range(n + 1):
#         if i not in arr:
#             return i


# arr1 = [3, 0, 1, 4]

# print(missingNumber(arr1))


# TASK R
# def calculate(expr):
#     a, operator, b = expr.split(" ")
#     if operator == "+":
#         return int(a) + int(b)
#     if operator == "-":
#         return int(a) - int(b)
#     if operator == "*":
#         return int(a) * int(b)
#     if operator == "/":
#         return int(a) / int(b)
#     raise ValueError("Invalid operator")


# task Q
# def hasProperty(obj, objKey):
#     for key in obj:
#         if key == objKey:
#             print(f"object has -> {objKey} <- property")
#             return True
#     print(f"object does not have -> {objKey} <- property")
#     return False


# car = {"name": "BMW", "year": 2004}

# print(hasProperty(car, "origin"))
# print(hasProperty(car, "name"))


# task P
# def objectToArray(obj):
#     result = []
#     for key in obj:
#         result.append([key, obj[key]])
#     return result


# print(objectToArray({"Name": "Alex", "age": 22, "d": 234, "group": "A2"}))


# task O
# def calculateSumOfNumbers(arr):
#     total = 0

#     for item in arr:
#         if type(item) == int or type(item) == float:
#             total += item

#     return total


# print(calculateSumOfNumbers([True, 25, 4.6, 28]))


# Task N
# def palindromCheck(text):
#     text1 = text.lower()[::-1]
#     return text.lower() == text1


# result1 = palindromCheck("pyhon")
# result2 = palindromCheck("ddddddddddddd")
# print(result2)


# TASK M
# def numberSquare(n):
#     return list(map(lambda num: {
#         "number": num,
#         "square": num ** 2
#     }, n))


# numbers = list(num for num in range(10))

# print(numberSquare(numbers))


# def reverseSentence(str):
#     str = str.lower()
#     list1 = str.split(" ")
#     print(list1)
#     reversed_words = []
#     for word in list1:
#         reversed_words.append(word[::-1])

#     return " <--> ".join(reversed_words)


# print(reverseSentence("we like coding!"))
# print(reverseSentence("Burak project"))
