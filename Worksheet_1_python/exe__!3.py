def str_replace(str_input, find, replace_with):
    result=[]
    result.append(str_input.replace(find,replace_with))
    return ' '.join(result)

def main():
    str_input=input("Enter a string: ")
    ch_find=input("Enter a character to search and replace: ")
    ch_replace=input("Enter a character to replace with: ")
    if not str_input or not ch_find or not ch_replace:
        print("Invalid inputs, You have not entered all the required inputs")
    elif str_input.count(ch_find)==0:
        print (ch_find, "Character not found in given string", str_input)
    else:
        out_put=str_replace(str_input,ch_find,ch_replace)
        print("The output after replacing a character in given string is: ", out_put)

if __name__=='__main__':
    main()
