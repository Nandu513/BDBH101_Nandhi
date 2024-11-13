def str_sort(str_list):
    y = sorted(str_list, key=lambda x: x[-1])
    return y
if __name__ == '__main__':
    string_list = ["apple", "banana", "cherry", "date"]
    print(str_sort(string_list))
