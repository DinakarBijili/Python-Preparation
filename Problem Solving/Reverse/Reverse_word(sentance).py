
"""Reverse of word(sentance)"""
def reverse_of_word(sentance):
    words = sentance.split()
    words.reverse()
    return " ".join(words)
char = input("Enter Sentance you want  to reverse : ")
result = reverse_of_word(char)
print("Reverse of words =",result)
