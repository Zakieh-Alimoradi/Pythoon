def tabe(text):
    words = text.split()
    list = []

    for word in words:
        if not list or word != list[-1]:
            list.append(word)

    return ' '.join(list)

text = input("Please enter your text: ")
cleaned = tabe(text)
print("Cleaned text:", cleaned)