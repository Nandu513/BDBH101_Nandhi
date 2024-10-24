x=[1,5,6,3,2,1,7,9,9,5]
print(f'Input: {x}')
d=int(input("Enter a element you want to be deleted completely: "))
if d not in x:
    print(f'{d} is not in the list')
else:
    res=[ i for i in x if i!=d ]
    print(f'Output: after deleting all occurrence of {d} is: {res}')
