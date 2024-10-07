def highest_frequent_in_string(str_unq, input_string):
    count = []
    for char in str_unq:
        count_time = 0
        for i in range(len(input_string)):
            if input_string[i] == char:
                count_time += 1
        count.append(count_time)
    return count

def main():
    string_input = input("Enter a string: ")
    str_input=string_input.replace(" ","")
    non_duplicate_string = ""
    for char in str_input:
        if char not in non_duplicate_string:
            non_duplicate_string += char
    print(non_duplicate_string)
    check = highest_frequent_in_string(non_duplicate_string, str_input)
    print(check)
    max_repeat = check[0]
    print("Most repeated are: ")
    for i in range(len(check)):
        if check[i] >= max_repeat:
            print(non_duplicate_string[i], "character", "Repeated: ", check[i])
            max_repeat = check[i]
        else:
            max_repeat = check[0]

if __name__ == "__main__":
    main()
