x=[1,5,6,3,2,1,7,9,9,5]
print(f'Input: {x}')
k=int(input("How many times repeated element, you are searching for: "))
if k==0:
    print('Please enter a number greater than 0.')
else:
    d=[i for i in set(x) if x.count(i)== k]
    if not d:
        print(f"No elements found which are repeated {k} times")
    else:
        print(f'Output: list of only {k} times repeated elements in given list is: {d}')
