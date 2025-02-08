def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ""
    for word in words[::-1]:
        reversed_sentence += word + " "
    return reversed_sentence.strip()
