from translate import Translator

#
f = open('ex_4.txt', 'r')
s = list(f.readlines())
f.close()

s = [line.rstrip() for line in s]

for el in s:
    translator= Translator(to_lang="ru")
    translation = translator.translate(el)
    print (translation)

