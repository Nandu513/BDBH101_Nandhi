def find_even(num_list):
    x=[i for i in num_list if i%2==0]
    return x
def main():
    num=[2,11,43,56,78,98,91,65,72]
    print(f'Input: {num}')
    if not find_even(num):
        print('Output: No even number found in given list')
    else:
        print("Output: The even numbers in given list are: ", find_even(num))
if __name__ == "__main__":
    main()
