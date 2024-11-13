def dict_num(num_list):
    dict_no= {x: x ** 2 for x in num_list if x % 2 == 0}
    return dict_no
if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result= dict_num(numbers)
    print(result)
