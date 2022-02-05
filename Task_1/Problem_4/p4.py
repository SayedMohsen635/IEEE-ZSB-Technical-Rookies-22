# Frame Method
def frame(sentence):
    size = len(max(sentence , key = len))
    print('*' * (size + 4))
    for word in sentence:
        print('* {a:<{b}} *'.format(a=word, b=size))
    print('*' * (size + 4))

# Program Test
sentence = input("Write the sentence --> ")
frame(sentence.split(" "))