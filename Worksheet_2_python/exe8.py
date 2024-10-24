m=['hi','hello','karan','welcome','kidos']
print(f'Input: {m}')
l=[i for i in m if i[0]=='k']
if not l:
    print('No words starts with k letter found, in given list of strings')
else:
    print(f'Output: words from a string list,whose first character is k are:')
    print(l)
