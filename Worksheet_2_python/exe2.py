def find_max(num_list):
    max=num_list[0]
    for i in num_list:
        if i>max:
            max=i
    return max
def find_min(num_list):
    min=num_list[0]
    for i in num_list:
        if i<min:
            min=i
    return min
def main():
    num=[20,3,77,54,23,1]
    print(f'Input: {num}')
    print(f'Output:')
    print("The max number in given list is: ", find_max(num))
    print("The min number in given list is: ", find_min(num))

if __name__ == '__main__':
    main()
