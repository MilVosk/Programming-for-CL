word = ''
allWords = []
while True:
    word = input('Enter a word: ')
    if word == 'done':
        all = ''.join(allWords)
        break
    allWords.append(word)
a = sorted(allWords)
for allWords in a:
    print('{0} comes first in the dictionary'.format(a[0]))
    print('{0} comes last in the dictionary'.format(a[-1]))
    break
