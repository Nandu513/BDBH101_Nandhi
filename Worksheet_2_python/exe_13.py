test_dict = {"Gfg" : [5, 7, 7, 7, 7], "is" : [6, 7, 7, 7], "Best" : [9, 9, 6, 5, 5]}
print(f'Input: {test_dict}')
val_list=[]
keys=[]
for key,values in test_dict.items():
    val_list.append(values)
    keys.append(key)
# print(val_list)
# print(keys)
x=False
for i in range(len(val_list)-1,0,-1):
    if len(set(val_list[i]))>len(set(val_list[i-1])):
        x=True
        print (f'Output: Max unique elements are found in the key: {keys[i]}')
        
if not x:
    print('No unique elements found in values of the key')
