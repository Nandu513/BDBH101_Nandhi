dict_sum_values={'one':1,'two':2,'three':3,'four':4,'five':5}
print(f'Input: {dict_sum_values}')
sum=0
for val in dict_sum_values.values():
    sum+=val
print(f'Output: The sum of all values in dict is: {sum}')
