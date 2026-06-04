# task P
def objectToArray(obj):
    result = []
    for key in obj:
        result.append([key, obj[key]])
    return result


print(objectToArray({"Name": "Alex", "age": 22, "d": 234, "group": "A2"}))


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
