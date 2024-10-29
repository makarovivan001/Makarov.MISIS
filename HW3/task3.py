def count_word(text):
    words = text.replace("n", " ").split()

    
    s1 = {}
    result = []
    for word in words:
        word = word.lower().strip(",.;'""")
        count = s1.get(word, 0)
        result.append(count)
        s1[word] = count + 1
    
    return result

text = """She sells sea shells on the sea shore;
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,
I'm sure that the shells are sea shore shells."""



result = count_word(text)
print(' '.join(map(str, result)))