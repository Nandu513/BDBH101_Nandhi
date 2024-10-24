def find_duplicates(a):
    x=[a[i]  for i in range(0,len(a)-1) for j in range(i+1,len(a)) if a[i]==a[j] ]
    if not x:
        print('Output: No duplicates found')
    else:
        print("Output: The duplicates in given list are: ", x)
if __name__=="__main__":
    # x=[1,9,8,1,2,6,2,4,5,4,3,7,8,7,3,3]
    y=[1,1,2,3,3,4,5,6,6]
    print(f'Input: {y}')
     # find_duplicates(x)
    find_duplicates(y)
