
def replace_word():
    str = 'Hi guys, i am Fargod and *****'
    print(str)
    word_to_replace = input('Enter the word to replace: ')
    word_replcement = input('Enter thew word replacement: ')
    print(str.replace(word_to_replace,word_replcement))


replace_word()