# TASK M
def numberSquare(n):
    return list(map(lambda num: {
        "number": num,
        "square": num ** 2
    }, n))


numbers = list(num for num in range(10))

print(numberSquare(numbers))


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
