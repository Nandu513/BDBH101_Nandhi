a= [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(f'Input: {a}')
def insertion_sort(a):
    for i in range(1, len(a)):
        key=a[i]
        j=i-1
        while j>-1 and a[j]>key:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
    print(f'Output: sorted list in ascending order: {a}')
insertion_sort(a)
