def rm_spaces(str_input):
    str_input=str_input.lstrip()
    print("length of string after removing leading spaces: ",len(str_input))
    return str_input

def main():
    str_input=input("Enter a string: ")
    if not str_input or str_input.strip()=='':
        print("String is empty")
    else:
        print(len(str_input), "length of string before removing leading white spaces")
        result=rm_spaces(str_input)
        print(result)

if __name__=='__main__':
    main()
