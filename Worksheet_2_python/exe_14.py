sentence='Hi this is is a a sentence with with duplicate no words words'
print(f'Input: {sentence}')
dict_sentence={i:sentence.split()[i] for i in range(len(sentence.split())) }
print(f'Sentence converted into dict: {dict_sentence}')
x=[]
for val in dict_sentence.values():
    if val not in x:
        x.append(val)
if sentence.split()==x:
    print(F"{sentence}: has no duplicate words in it")
else:
    print(f'Output: {' '.join(x)}')
