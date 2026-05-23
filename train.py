def reverseSentence(str):
    str = str.lower()
    list1 = str.split(" ")
    print(list1)
    reversed_words = []
    for word in list1:
        reversed_words.append(word[::-1])

    return " <--> ".join(reversed_words)


print(reverseSentence("we like coding!"))
print(reverseSentence("Burak project"))
